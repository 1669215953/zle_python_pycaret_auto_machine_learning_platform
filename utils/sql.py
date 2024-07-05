import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:1314@localhost/flask_python?charset=utf8mb4')
def save_csv(file=r'D:\codeprogram\Python_homework\Python_flask_web\python_flask_project\app\spider\BOSS直聘.csv'):
    # 读取CSV文件
    data = pd.read_csv(file)
    # 创建MySQL数据库连接
    # 将数据插入到MySQL数据库中的表中
    data.to_sql('job_info', engine, if_exists='replace', index=False)
    print("数据导入成功！")
def get_all_data():
    # Create a database connection
    conn = engine.connect()

    try:
        # Execute a SQL query to retrieve all data from the 'job_info' table
        query = "SELECT * FROM job_info"
        result = conn.execute(query)

        # Fetch all rows from the query result
        rows = result.fetchall()

        # Convert the rows to a pandas DataFrame
        columns = result.keys()
        data = pd.DataFrame(rows, columns=columns)

        # Close the database connection
        conn.close()

        return data
    except Exception as e:
        # Handle any exceptions that occur during the process
        print("发生错误:", str(e))
        conn.close()
        return None



def get_job_reward():
    '''
    获取工作福利
    '''
    # Create a database connection
    conn = engine.connect()

    # Execute a SQL query to retrieve the 'job_reward' column from the 'job_info' table
    query = "SELECT 福利待遇 FROM job_info"
    result = conn.execute(query)

    # Fetch all rows from the query result
    rows = result.fetchall()

    # Close the database connection
    conn.close()

    # Extract the job rewards from the rows
    job_rewards = [row[0] for row in rows]

    return job_rewards

    
    return data
if __name__=='__main__':
    save_csv()
    #print(get_job_reward())
    print(type(get_all_data()))#pandas.core.frame.DataFrame