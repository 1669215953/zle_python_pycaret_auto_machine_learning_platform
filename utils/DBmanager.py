import json
import pymysql
from utils.DataManager import Params
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
            sql = "SELECT json_data FROM history WHERE user_id = %s AND mission_id = %s"
            cursor.execute(sql, (userId, missionId))
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
    def Init_mission_json_data(self,userId,missionId,user_params=None):#初始化用户参数表 需要重写
        if user_params is  not None:
              data=Params()
              DBmanager.add_or_update_history_json(userId,missionId,data.Init_by_web_data(user_params))
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

if __name__ == '__main__':
    with open("test.json", "r") as file:
        history = json.load(file)
        DBmanager.add_or_update_history_json(123,123,history)

