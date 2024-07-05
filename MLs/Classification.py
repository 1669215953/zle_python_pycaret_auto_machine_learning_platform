import os
import pandas as pd
from pycaret.classification import *
import json
import copy
import logging
from utils.setting import *
from utils.DataManager import Planet,DBmanager,Params
logging.getLogger('lightgbm').setLevel(logging.ERROR)

class AutoMLPipeline:
    #用户配置参数  数据路径  性能图片 保存路径
    def __init__(self,userId=1,missionId=1):
        param=Params()
        param.Init_by_sql(userId,missionId)
        self.history=param
        self.params = self.history.get_pycaret_params()
        self.save_path=self.history.get_save_path()
        self.model_dir=self.history.get_model_dir()
        self.model = None
        self.setup_models_data=None       #PyCaret 整个设置环节的日志信息，这包括数据预处理的步骤、特征工程的信息以及其他配置参数的详情
        self.compare_models_data = None #DataFrame，它包含了在比较模型阶段各种不同算法的性能指标，比如准确度、AUC 值、召回率等
        self.create_model_data = None #得到的是创建的模型的性能指标，这通常包括交叉验证的结果和各种评估指标。
        self.tune_model_data = None #得到调优过程的详细结果和指标
        self.predictions = None   #预测测试数据
    def Init(self,userId=1,missionId=1):
        param=Params()
        param.Init_by_sql(userId,missionId)
        self.history=param
        self.params = self.history.get_pycaret_params()
        self.save_path=self.history.get_save_path()
        self.model_dir=self.history.get_model_dir()
        self.model = None
        self.setup_models_data=None       #PyCaret 整个设置环节的日志信息，这包括数据预处理的步骤、特征工程的信息以及其他配置参数的详情
        self.compare_models_data = None #DataFrame，它包含了在比较模型阶段各种不同算法的性能指标，比如准确度、AUC 值、召回率等
        self.create_model_data = None #得到的是创建的模型的性能指标，这通常包括交叉验证的结果和各种评估指标。
        self.tune_model_data = None #得到调优过程的详细结果和指标
        self.predictions = None   #预测测试数据
    def collect_model_info(self):
        """收集模型相关信息，并将其格式化为字典形式。"""
        model_info = {
        'setup_models_data': json.loads(self.setup_models_data.to_json(orient='records')),
        'compare_models_data': json.loads(self.compare_models_data.to_json(orient='records')),
        'create_model_data': json.loads(self.create_model_data.to_json(orient='records')),
        'tune_model_data': json.loads(self.tune_model_data.to_json(orient='records')),
        'predictions': json.loads(self.predictions.to_json(orient='records')) if self.predictions is not None else None
        }
        self.history.MLinfo=model_info
        self.history.save_history()
        #print(model_info)
        return model_info
    def collect_history_info(self):
        """收集模型相关信息，并将其格式化为字典形式。"""
        model_info = {
        'setup_models_data': json.loads(self.setup_models_data.to_json(orient='records')),#配置环境等
        'compare_models_data': json.loads(self.compare_models_data.to_json(orient='records')),
        'create_model_data': json.loads(self.create_model_data.to_json(orient='records')),
        'tune_model_data': json.loads(self.tune_model_data.to_json(orient='records')),
        'predictions': json.loads(self.predictions.to_json(orient='records')) if self.predictions is not None else None
        }
        self.history.MLinfo=model_info
        #字典 保存到数据库
        self.history.save_history()
        return model_info
    #除了 都是pandas.DataFrame   
    def print_pipeline_results(self):
        print("Setup Data:")
        print(self.setup_models_data)
        print("\nCompare Models Data:")
        print(self.compare_models_data)
        print("\nCreate Model Data:")
        print(self.create_model_data)
        print("\nTune Model Data:")
        print(self.tune_model_data)
        print("\nPredictions:")
        print(self.predictions)
        
    def run_setup(self):
        if 'setup' in self.params:
            setup_params = self.params['setup']
            print(setup_params)
            self.model = setup(**setup_params)
            self.setup_models_data= pull()
            #print("self.setup_models_data= pull()\n", (self.setup_models_data))


    def run_compare_models(self):
        if 'compare_models' in self.params:
            compare_params = self.params['compare_models']
            try:
              self.model = compare_models(**compare_params)
            except Exception as e:
                print("GGBO")
            self.compare_models_data= pull()
            #print("self.compare_models_data= pull()\n", self.compare_models_data.to_json(orient='records'))

    def run_create_model(self):
        if 'create_model' in self.params:
            create_params = self.params['create_model']
            self.model = create_model(**create_params)
            self.create_model_data= pull()
            #print("self.create_model_data= pull()\n", self.create_model_data)

    def run_tune_model(self):
        if 'tune_model' in self.params and self.model is not None:
            tune_params = self.params['tune_model']
            self.model = tune_model(self.model, **tune_params)
            self.tune_model_data=pull()
            #print("self.tune_model_data= pull()\n", self.tune_model_data)

    def run_predict_model(self):
        if self.history.get_path(Planet.test):
         print("预测路径",self.history.get_path(Planet.test))
         try:
            predictions = predict_model(self.model,data = pd.read_csv(self.history.get_path(Planet.test)))
            self.predictions= predictions
            predictions.to_csv(self.history.get_path(Planet.predictfile), index=False)
         except Exception as e:
             print("预测错误",e)
        
    def run_plot_model(self):
        if 'plot_model' in self.params and self.model is not None:
            plot_params = self.params['plot_model']
            # 保存当前的工作目录
            current_directory = os.getcwd()
            # 尝试更改工作目录到指定的保存路径
            try:
                os.makedirs(self.save_path, exist_ok=True)  # 确保目录存在
                os.chdir(self.save_path)  # 更改工作目录

                # 在新的工作目录中生成并保存图表
                plot_model(self.model,**plot_params)
                print(f"Plot saved to: {self.save_path}")
            except Exception as e:
                print(f"Failed to save plot . Error: {e}")
            finally:
                # 将工作目录改回原来的路径
                os.chdir(current_directory)

    def run_save_model(self):
        if 'save_model' in self.params and self.model is not None:
            save_params = self.params['save_model']
            
            save_params['model_name']=os.path.join(self.model_dir,save_params['model_name'])
            os.makedirs(self.model_dir, exist_ok=True)  # 确保目录存在
            save_model(self.model, **save_params)
    def execute_pipeline(self):
        #print("开始setup")
        self.run_setup()
        #print("开始run_compare_models")
        self.run_compare_models()
        #print("开始run_create_model")
        self.run_create_model()
        #print("开始run_tune_model")
        self.run_tune_model()
        #print("开始run_plot_model")
        self.run_plot_model()
        #print("开始run_save_model")
        self.run_save_model()
        #self.print_pipeline_results()
        self.run_predict_model()
        self.collect_history_info()
def get_predict(params:Params):
    try:
        print("路径",params.get_path(Planet.modelpath))
        saved_model = load_model(params.get_path(Planet.modelpath))
        predictions = predict_model(saved_model,data=params.get_df_data(Planet.test))
        predictions.to_csv(params.get_path(Planet.predictfile), index=False)
        predictions=json.loads(predictions.to_json(orient='records'))
        history=DBmanager.get_history(**params.get_uerId_and_missionId())
        history["predictions"]=predictions
        DBmanager.add_or_update_history_json(**params.get_uerId_and_missionId(),history=params.turn_history())
        return predictions
    except Exception as e:
       print("Error",e)
# 用户配置示例
