from pymysql import *
# 建立数据库连接
cnx = connect(
    host="localhost", 
    port=3306,
    user='root',
    password='1314',
    database='flask_python'
)

# 创建游标对象
cursor = cnx.cursor()


def query(sql, params,type='no select'):
    params = tuple(params)
    # 执行查询语句
    cursor.execute(sql, params)
    cnx.ping(True)
    # 获取查询结果
    if type != 'no select':#查询
        data_list = cursor.fetchall()
        # 提交事务
        cnx.commit()
        return data_list
    else:
        cnx.commit()

