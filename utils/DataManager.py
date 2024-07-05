import copy
from enum import Enum
import json
import pandas as pd
import os
from utils.setting import *
from utils.setting import *
import datetime
def is_json(data):
    try:
        json.loads(data)
    except ValueError:
        return False
    return True


class Params:
    def __init__(self):
        self.user_info={"userId":None,"missionId":None,"mlclass":None,"create_time": str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))}#用户信息自己保存
        self.MLinfo={
        'setup_models_data': None,
        'compare_models_data': None,
        'create_model_data': None,
        'tune_model_data':None,
        'predictions': None
        }#模型生成数据
        self.userparams = {}#用户选择参数 前端传回 直接用于pycaret
    #前端只会传user_info userparams其他是训练得到
    def Init_by_history(self,history):
        self.user_info = history["user_info"]
        self.MLinfo = history["MLinfo"]
        self.userparams = history["userparams"]
        print(history)
    def Init_by_web(self,user_info,userparams):
        self.user_info=user_info#用户信息自己保存
        self.MLinfo={
        'setup_models_data': None,
        'compare_models_data': None,
        'create_model_data': None,
        'tune_model_data':None,
        'predictions': None
        }#模型生成数据
        self.userparams = userparams#用户选择参数 前端传回 直接用于pycaret
    def Init_by_web_data(self,web_data):
        self.user_info=web_data["user_info"]#用户信息自己保存
        self.MLinfo={
        'setup_models_data': None,
        'compare_models_data': None,
        'create_model_data': None,
        'tune_model_data':None,
        'predictions': None
        }#模型生成数据
        self.userparams = web_data["userparams"]#用户选择参数 前端传回 直接用于pycaret
    def Init_by_sql(self,userId,missionId):
        history=DBmanager.get_history(userId,missionId)
        if history is None:
            print("未找到数据")
            return None
        # 从history字典中获取相应的值
        self.user_info = history["user_info"]
        self.user_info={"userId":userId,"missionId":missionId}
        self.MLinfo = history["MLinfo"]
        self.userparams = history["userparams"]
    def get_path(self,mode:Planet):
        if mode == Planet.test or mode == Planet.train:
                filepath = self.getfilepath(mode)
                print("多分子",filepath)
                if os.path.isfile(filepath):
                    return filepath
        elif mode == Planet.metrics:
            save_path = self.get_save_path()
            if os.path.isfile(save_path):
                return save_path
        elif mode == Planet.model:
            model_dir = self.get_model_dir()
            if os.path.isdir(model_dir):
                return model_dir
        elif mode == Planet.modelpath:
            model_path = self.get_model_path()
            print("模型路径",model_path+".pkl")
            if os.path.exists(model_path+".pkl"):
                return model_path
        elif mode == Planet.predictfile:
            userId,missionId=self.get_uerId_and_missionId()["userId"],self.get_uerId_and_missionId()["missionId"]
            predict_path = os.path.join(PREDICT_DIR,str(userId)+"_"+str(missionId)+"_predict.csv")
            print("预测路径",predict_path)
            return predict_path
        return None
    def get_predict_filepath(self):
        return PREDICT_DIR
    def get_model_path(self):
        print("模型路径1",os.path.join(self.get_model_dir(),self.userparams["save_model"]["model_name"]))

        return os.path.join(self.get_model_dir(),self.userparams["save_model"]["model_name"])
    def get_save_path(self):#性能图片
        return self.get_file_path(PLOTS_DIR)
    def get_model_dir(self):#模型保存
        return self.get_file_path(MODEL_DIR)
        #获取json数据
    def get_json_Init(self,user_params=None):
        if is_json(user_params):
            self.userparams=json.loads(user_params)
        elif isinstance(user_params, dict):
                return user_params  
        
    
            
    #转化为history数据 打包
    def turn_history(self):
        history={"user_info":self.user_info,
            "MLinfo":self.MLinfo,
            "userparams":self.userparams
        }
        return history
    #获取ID和 MID
    def get_uerId_and_missionId(self):
        return {
                "userId":self.user_info["userId"],
                "missionId":self.user_info["missionId"]
                }
    
    #保存history
    def save_history(self, history=None):
        if history is not None:
            return DBmanager.add_or_update_history_json(**self.get_uerId_and_missionId(),history=self.turn_history())
        try:
           return DBmanager.add_or_update_history_json(**self.get_uerId_and_missionId(),history=self.turn_history())
        except Exception as e:
           print("保存失败",e)
           return 0
    #转化为模型直接使用参数
    
    def get_pycaret_params(self):
        param=copy.deepcopy(self.userparams)
        param["setup"]["data"]=self.get_df_data(Planet.train)#获取模型
        return param
    
    def getfilepath(self,mode:Planet,string=None):
        if mode == Planet.train or string == "train":
            return os.path.join(self.get_file_path(UPLOAD_DIR),"train.csv")
        else:
            print("获取",os.path.join(self.get_file_path(UPLOAD_DIR),"test.csv"))
            return os.path.join(self.get_file_path(UPLOAD_DIR),"test.csv")
    
    #获取训练 验证
    def get_df_data(self,mode:Planet):
        try:
            print("测试机",self.get_path(mode))
            data=pd.read_csv(self.get_path(mode))
            return data
        except Exception as e:
            print("未成功读取DF",self.get_uerId_and_missionId(),e,"\n",self.get_path(mode))
       

    def get_file_path(self,filename):
        return os.path.join(get_U_M_path(filename=filename,**self.get_uerId_and_missionId()))
    
      
    def __str__(self):
        return json.dumps(self.turn_history())
import json
import pymysql
class MySQLManager:
    def __init__(self, config_file):
        with open(config_file, 'r') as f:
            config = json.load(f)
        self.connection = pymysql.connect(
            host=config['host'],
            user=config['user'],
            password=config['password'],
            db=config['database']
        )
    def register_user(self, username, password):
        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO user (username, password) VALUES (%s, %s)"
                cursor.execute(sql, (username, password))
            self.connection.commit()
            if cursor.rowcount > 0:
                return 1  # 注册成功
            else:
                return 0  # 注册失败
        except Exception as e:
            print(f"注册过程中发生错误: {e}")
            return 0  # 如果出现异常，视为注册失败
        

    def add_or_update_history_json(self, userId, missionId, history):
        print("初始化",userId,missionId, history)
        try:
            if isinstance(history, dict):
                history = json.dumps(history)
                print(history)
            with self.connection.cursor() as cursor:
                sql = """
                INSERT INTO history (user_id, mission_id, json_data)
                VALUES (%s, %s, %s)
                ON DUPLICATE KEY UPDATE json_data = VALUES(json_data)
                """
                cursor.execute(sql, (userId, missionId, history))
                
            self.connection.commit()
            
            if cursor.rowcount > 0:
                return 1  # 上传成功 或 更新成功
            else:
                return 0  # 上传失败 或 更新失败
        except Exception as e:
            print(f"上传过程中发生错误: {e}")
            return 0  # 如果出现异常，视为注册失败
    
    def get_user_id_by_username(self,username):
        result = DBmanager.query("SELECT id FROM user WHERE username = %s", [username], 'select')
        if result:
            return int(result[0][0])
        else:
            return None
    def get_task_count_by_user_id(self,user_id):
        result = DBmanager.query("SELECT COUNT(*) FROM history WHERE user_id = %s", [user_id], 'select')
        if result:
            return int(result[0][0])
        else:
            return None
    def get_taskidlist_by_user_id(self,user_id):
            result = DBmanager.query("SELECT mission_id FROM history WHERE user_id = %s", [user_id], 'select')
            if result:
                return result
            else:
                return None
            
    def check_password(self, username, password):
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM user WHERE username = %s and password = %s"
            cursor.execute(sql, (username, password))
            result = cursor.fetchone()
        return result is not None
    def  query(self,sql,params,type='no select'):
         with self.connection.cursor() as cursor:
            params = tuple(params)
            # 执行查询语句
            cursor.execute(sql, params)
            self.connection.ping(True)
            # 获取查询结果
            if type != 'no select':#查询
                data_list = cursor.fetchall()
                # 提交事务
                self.connection.commit()
                return data_list
            else:
                self.connection.commit()
        
    def get_history(self, userId, missionId, return_json=False):
        with self.connection.cursor() as cursor:
            print(f"数据库获取{userId}，{missionId}用户的数据")
            sql = "SELECT json_data FROM history WHERE user_id = %s AND mission_id = %s"
            cursor.execute(sql, (str(userId), str(missionId)))
            result = cursor.fetchone()
            
        # 如果没有查询到结果，返回 None
        if result is None:
            return None
        
        # 如果需要返回 json，直接返回
        if return_json:
            return result[0]
        
        # 否则，尝试将 JSON 解析为 dict
        try:
            return json.loads(result[0])
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None
    
    def close(self):
        self.connection.close()
    def Init_mission_json_data(self,userId,missionId,user_params=None):
        
        if user_params is  not None:
              data=Params()
              data.Init_by_web_data(user_params)
              DBmanager.add_or_update_history_json(userId,missionId,data.turn_history())
        else :
          with open("test.json", "r") as file:
            history = json.load(file)
            DBmanager.add_or_update_history_json(userId,missionId,history)
            
    def get_Params(self,userId, missionId, return_json=False):
        histroy=self.get_history(userId=userId, missionId=missionId, return_json=return_json)
        data=Params()
        data.Init_by_history(histroy)
        return data
        
        
DBmanager = MySQLManager('config.json')