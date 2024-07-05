import json
from flask import Flask,redirect,render_template,request,send_file, jsonify,Response,send_from_directory, abort,session
from flask_cors import cross_origin
from prompt_toolkit import HTML
from werkzeug.utils import secure_filename
from flask_cors import CORS
import zipfile
from werkzeug.utils import safe_join
import io
import os
from pycaret.classification import *
import threading
from MLs.MLmanager import PycaretManager,MLClass,get_ml_class
from utils.DataManager import DBmanager
from utils.setting import *
import pandas as pd
from utils.GPT import *
from io import StringIO
from utils.mainindex import DataFrame2Array, dropColumns
from utils.setting import *
import concurrent.futures
from utils.setting import *

app= Flask(__name__)
from veiws.user import user
app.register_blueprint(user.ub)
userfilepath="userfiles"
Pymanager=PycaretManager()
MLManager=None
app.config['SECRET_KEY'] = 'djaskldjkslajdklsal'
CORS(app)

'''
#性能图片获取测试
http://127.0.0.1:5000/metrics/test   #性能指标图片
#GPT 和 任务配置
http://127.0.0.1:5000/AI       #配置表 AI对话
#数据集上传
http://127.0.0.1:5000/up_data       #上传文件页面
#用户操作首页
http://127.0.0.1:5000/Df       #用户主页面表格
http://127.0.0.1:5000/Df/0       #用户主页面表格  数据展示
http://127.0.0.1:5000/Df/typography      #用户页面性能展示
http://127.0.0.1:5000/Df/tables      #用户页面性能展示

http://127.0.0.1:5000/api/get_model_info        #获取预测结果
http://127.0.0.1:5000/api/get_model_info        #训练过程数据

http://127.0.0.1:5000/download_model/best_model    #模型下载
'''

def parse_u_m():
    userId,missionId=request.get_json()["userId"],request.get_json()["missionId"]
    print("获取",userId,missionId)
    return userId,missionId

#待完善解析前端发来的用户数据 先得到任务类别 根据类别生成动态参数表
def get_paras(mlclass):
    return {
   "user_params": [
        {
          "AUC": {
            "mode":"input",
            "default":"88.1"
          },
          "Accuracy":{
            "mode": "checkbox",
            "default":"checked"
          },
          "F1": {
            "mode": "select",
            "select_item":["one","two","three"],
            "default":"one"
          }
        },
        {
          "Precision": {
            "mode":"input",
            "default":"0.9"
          },
          "Recall":{
            "mode": "checkbox",
            "default":"checked"
          },
          "F2": {
            "mode": "select",
            "select_item":["four","five","six"],
            "default":"four"
          }
        },
        {
          "MCC": {
            "mode":"input",
            "default":"0.1"
          },
          "Kappa":{
            "mode": "checkbox",
            "default":"checked"
          },
          "F3": {
            "mode": "select",
            "select_item":["seven","eight","nine"],
            "default":"seven"
          }
        }
      ]
}

#--------------------------utils--------------------------------------

@app.route('/api/userId')
def parse_u():
    name=session['username'] 
    print("用户名",name)
    userId=DBmanager.get_user_id_by_username(name)
    return jsonify({"userId": userId})



#--------------------------数据预览区--------------------------------------
#数据预览
@app.route('/data_view/<int:index>')
def data_view(index):
    path = ["userfiles/11/1/train.csv",
            "userfiles/11/2/train.csv",
            "userfiles/11/3/train.csv",
            "userfiles/11/4/train.csv",
            "userfiles/11/5/train.csv",
            "userfiles/11/6/train.csv",
            "userfiles/11/7/train.csv",
            "userfiles/housing.csv",
            ]

    with open(path[index], 'r') as f:
        text = StringIO(f.read())

    demo_df = pd.read_csv(text, sep=',')

    # pd.set_option('colheader_justify', 'center')  # FOR TABLE <th>
    print(index)
    return render_template('data_view.html', data_frame=demo_df.to_html(classes='table tablesorter'), index=index)

#数据预览
@app.route('/api/get_data_info',  methods = ['GET'])
def get_data_info():
    userId,missionId=parse_u_m()
    params=DBmanager.get_Params(userId,missionId)
    pddata=pd.read_csv(params.getfilepath(Planet.train))
    label=pddata.columns.tolist()
    null_sum = pddata.isnull().sum().to_dict()
    labeltype=pddata.dtypes.apply(lambda x: x.name).to_dict()
    describe=pddata.describe().to_dict()
    return jsonify({"label": label,"labe_type":labeltype,"null_num":null_sum,"describe":describe})

# new.js 中需要用来请求数据 => 来选择第几个数据集的路径
@app.route('/api-getDataSet', methods = ['POST', 'GET'])
def getDataSet():

    if request.method == 'POST':

        data = json.loads(str(request.data, 'utf-8'))
        path = ["userfiles/11/1/train.csv",
            "userfiles/11/2/train.csv",
            "userfiles/11/3/train.csv",
            "userfiles/11/4/train.csv",
            "userfiles/11/5/train.csv",
            "userfiles/11/6/train.csv",
            "userfiles/11/7/train.csv",
            "userfiles/housing.csv",
            ]

        with open(path[data], 'r') as f:

            text = StringIO(f.read())

        df = pd.read_csv(text, sep=',')

        if ("Unnamed: 0" in df.columns): df = dropColumns(df, columns=["Unnamed: 0"])

        res = DataFrame2Array(df)

        return str(res)

    return '<h1>请使用POST方法访问</h1>'






#--------------------------性能展示区--------------------------------------

#登录页面
@app.route('/metrics_view')
def metrics_view():
    return render_template('metrics_view.html')
#--------------------------任务操作区--------------------------------------

#任务操作页面
@app.route('/mission_view')
def mission_view():
    return render_template('mission_view.html')
#请求任务列表
@app.route('/api/mission_list')
def mission_list():
    userId=request.get_json()["userId"]
    data=DBmanager.get_taskidlist_by_user_id(userId)
    return  jsonify(list=data)


#--------------------------参数配置区--------------------------------------

@app.route('/api/user_paras')
def user_paras():
    mlclass=request.get_json()["mlcass"]
    data=get_paras(mlclass)
    return  jsonify(data)





#--------------------------路由区-------------------------------------

#登录页面
@app.route('/')
def user_login():
    return redirect('/user/login')

#GPT回答
@app.route('/get_AI', methods=['GET'])
def get_AI():
    data = request.args
    user_message = {'role': 'user', 'content': data.get('message')}
    print("用户",user_message)
    #successful, ai_response = gpt_35_api_stream([user_message])
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # 提交任务给线程池
        future = executor.submit(gpt_35_api_stream,[user_message])
        successful, ai_response = future.result()
        # 等待任务完成并获取结果
    print("AI回答",successful, ai_response)
    print("返回",ai_response)
    if not successful:
        return jsonify(error=ai_response)
    
    # Return the AI's response, which is the last message in the list.
    return jsonify(ai_response=ai_response)
#---------------------上传-------------------------------------------
#允许上传的文件类型
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif','csv','xls'} # 仅允许图片类型，可根据需要进行修改
    print('.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS)
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
#用户自定义上传数据接口
@app.route('/upload', methods=['POST'])
def upload_file():
    print("用户自定义上传")
    # 检查是否有文件字段
    if 'image' not in request.files:
        return '没有 image 字段在表单中'

    files = request.files.getlist('image')
    print(files)
    if not files:
        return '没有选择文件'

    filenames = []
    for file in files:
        print("Filename: ", file.filename)   # 打印文件名
        print("Filesize: ", len(file.read()))  # 打印文件大小
        file.seek(0)  # 移动文件指针回到文件开始位置

        if allowed_file(file.filename):
            # 创建图片保存目录，如不存在则创建
            userId=DBmanager.get_user_id_by_username(session['username'])
            missionId=DBmanager.get_task_count_by_user_id(userId)+1
            if not os.path.exists(path:=os.path.join(UPLOAD_FOLDER,str(userId),str(missionId))):
                # 如果路径不存在，使用os.makedirs()创建路径
                os.makedirs(path)
                print(f"路径已创建：{path}")
            else:
                print(f"路径已存在：{path}")
            
            filepath=os.path.join(UPLOAD_FOLDER,str(userId),str(missionId),file.filename)
            file.save(filepath)
            #开始进行训练
            #用户参数后面传
            #userId=DBmanager.get_user_id_by_username(session['username'])
            #missionId=DBmanager.get_task_count_by_user_id(userId)+1
            #print(session['username'],userId,missionId)
            #DBmanager.Init_mission_json_data(userId,missionId)
            #global Pymanager
            #Pymanager.Init(MLClass.classification,userId=userId,missionId=missionId)
            #thread = threading.Thread(target=run_in_thread,args=(userId,missionId)) 
            #thread.start()
            filenames.append(file.filename)
        else:
            return '文件格式不符合要求: %s' % file.filename
    return '上传成功！文件名：%s' % ', '.join(filenames)

#选择默认项目后的 开始训练接口
@app.route('/up/<selectedOption>', methods=['GET'])
def select_default(selectedOption):
    print("用户默认数据集上传")
    userId,missionId=parse_u_m() 
    #DBmanager.Init_mission_json_data(userId,missionId)
    print(os.path.join(DEFAULT_DIR,str(selectedOption)),os.path.join(UPLOAD_FOLDER,str(userId),str(missionId)))
    copy_files(os.path.join(DEFAULT_DIR,str(selectedOption)),os.path.join(UPLOAD_FOLDER,str(userId),str(missionId)))       
    #global Pymanager
    #Pymanager.Init(MLClass.classification,userId=userId,missionId=missionId)
    #thread = threading.Thread(target=run_in_thread,args=(userId,missionId)) 
    #thread.start()
    return redirect('/Df/0')

#接受前端传来用户配置参数
@app.route('/api/get-userparams',methods=['GET','POST'])
def get_params_json():
    print("接受到用户参数")
    json_data = request.get_json()
    userId,missionId=json_data["user_info"]["userId"],json_data["user_info"]["missionId"]
    print(userId,missionId,"用户","\n参数:\n",json_data)
    DBmanager.Init_mission_json_data(userId,missionId,json_data)#使用用户参数上传数据库
    MLCLASS=get_ml_class(json_data["user_info"].get('mlclass'))
    global Pymanager
    Pymanager.Init(MLCLASS,userId=userId,missionId=missionId)
    thread = threading.Thread(target=run_in_thread,args=(userId,missionId)) 
    thread.start()
    return jsonify({"message":"success"})
#初始化文件
@app.route('/test.json',methods=['GET','POST'])
def get_json():
    return send_from_directory('.', 'test.json')
#-------------------wjh-ML ------------------------   
#下载模型
@app.route('/download_model', methods=['GET'])
def download_model():
    userId,missionId=parse_u_m()
    history=DBmanager.get_history(userId,missionId)
    return send_from_directory(get_U_M_path(userId,missionId,MODEL_DIR), history["userparams"]["save_model"]["model_name"]+".pkl")

#下载模型
@app.route('/download_predict', methods=['GET'])
def download_predict():
    userId,missionId=parse_u_m()
    return send_from_directory(PREDICT_DIR,str(userId)+"_"+str(missionId)+"_predict.csv")

#请求预测
@app.route('/api/get-predict',methods=['GET','POST'])
def post_predict():
    userId,missionId=parse_u_m()
    params=DBmanager.get_Params(userId,missionId)
    MLCLASS=get_ml_class(params.user_info.get('mlclass'))
    global Pymanager
    Pymanager.Init(MLCLASS,userId=userId,missionId=missionId)
    thread = threading.Thread(target=predict_in_thread,args=(params,)) 
    thread.start()
    return jsonify({"message":"success"})

#获取预测数据csv文件
@app.route('/api/get-predict-csv',methods=['GET','POST'])
def post_predict_csv():
    userId,missionId=parse_u_m()
    params=DBmanager.get_Params(userId,missionId)
    MLCLASS=get_ml_class(params.user_info.get('mlclass'))
    global Pymanager
    Pymanager.Init(MLCLASS,userId=userId,missionId=missionId)
    thread = threading.Thread(target=predict_in_thread,args=(params,)) 
    thread.start()
    return jsonify({"message":"success"})


#获取后端数据
#请求时需要json数据 {"userId":userId, "missionId":missionId}
@app.route('/api/get_model_info')
def get_model_info():
    file_path = 'history测试.json'
    return send_file(file_path, as_attachment=True)

# 提供接口获取metrics文件夹中的所有图片名字
@app.route('/api/metrics/file_list', methods=['GET'])
def get_file_list_new():
    folder_path = 'metrics'
    file_list = os.listdir(folder_path)
    return jsonify(file_list)

#请求图片接口
@app.route('/api/metrics/<filename>', methods=['GET'])
def get_file(filename):
    # 拼接文件路径
    file_path = 'metrics/' + filename
    # 检查文件是否存在
    if os.path.exists(file_path):
        # 发送文件到前端
        return send_file(file_path, as_attachment=True)
    else:
        return 'File not found'

#训练函数
def train(userId,missionId):
    global MLManager
    global Pymanager
    MLManager=Pymanager.Get_ML()
    MLManager.Init(userId,missionId)
    MLManager.execute_pipeline()
#预测
def predict(param):
    print("预测",param)
    global Pymanager
    Pymanager.Get_ML()
    Pymanager.get_predict(param)
#训练线程函数类方法
def run_in_thread(userId,missionId):
    train(userId,missionId)
def predict_in_thread(params):
    predict(params)

# @app.route('/getimgaetest')
# def hello_world0():
#     return render_template('getimage.html')
# @app.route('/images')
# def hello_world10():
#     return render_template('images.html')
# @app.route('/ml')
# def hello_world1():
#     return render_template('weather.html')
#选择 上传数据
@app.route('/up_data')
def hello_world3():
    return render_template('up_data2.html')
@app.route('/test copy')
def hello_world2():
    return render_template('test.html')
@app.route('/pd')
def hello_world4():
    return render_template('pd.html')
@app.route('/AI')
def AI():
    return render_template('AItalk.html')





#用户操作首页
@app.route("/Df")
def dataframe3():
    import numpy as np
    pd.set_option('display.width', 1000)
    pd.set_option('colheader_justify', 'center')
    np.random.seed(6182018)
    demo_df = pd.DataFrame({'date': np.random.choice(pd.date_range('2018-01-01', '2018-06-18', freq='D'), 50),
                            'analysis_tool': np.random.choice(['pandas', 'r', 'julia', 'sas', 'stata', 'spss'],50),              
                            'database': np.random.choice(['postgres', 'mysql', 'sqlite', 'oracle', 'sql server', 'db2'],50), 
                            'os': np.random.choice(['windows 10', 'ubuntu', 'mac os', 'android', 'ios', 'windows 7', 'debian'],50), 
                            'num1': np.random.randn(50)*100,
                            'num2': np.random.uniform(0,1,50),                   
                            'num3': np.random.randint(100, size=50),
                            'bool': np.random.choice([True, False], 50)
                        },
                            columns=['date', 'analysis_tool', 'num1', 'database', 'num2', 'os', 'num3', 'bool'])

    pd.set_option('colheader_justify', 'center')   # FOR TABLE <th>
    return render_template('user-index.html',data_frame=demo_df.head().to_html(classes='table tablesorter'))


# --------------------metrics play--------------------------

@app.route('/Df/typography')
def detail1():
    return send_file("templates/typography.html")

@app.route('/Df/tables')
def detail2():
    return send_file("templates/tables.html")

@app.route('/file_list', methods=['GET'])
def get_file_list():
    
    file_list = os.listdir(PLOTS_FOLDER)
    return jsonify(file_list)
#------------------User Main-------------------------

# index => 用户选择的第几个数据
@app.route("/Df/<int:index>")
def dataframe1(index):
    path = ["userfiles/forestfires.csv",
            "userfiles/housing.csv",
           "userfiles/forestfires.csv",
            "userfiles/housing.csv",
            "userfiles/forestfires.csv",
            "userfiles/housing.csv",
            "userfiles/forestfires.csv",
            "userfiles/housing.csv",
            "userfiles/forestfires.csv",
            "userfiles/housing.csv",
            ]

    with open(path[index], 'r') as f:
        text = StringIO(f.read())

    demo_df = pd.read_csv(text, sep=',')

    pd.set_option('colheader_justify', 'center')   # FOR TABLE <th>
    print(index)
    return render_template('user-index.html',data_frame=demo_df.to_html(classes='table tablesorter'), index=index)




if __name__ == "__main__":
    app.run()

