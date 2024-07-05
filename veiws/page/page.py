from flask import Flask,session,render_template,redirect,Blueprint,request,jsonify
from utils.getHmoeData import *
from utils.data_deal import *
from flask_cors import cross_origin
import random

pb = Blueprint('page',__name__,url_prefix='/page',template_folder='templates')
data_loader=Dataloader('人工智能_liepindata.csv')
@pb.route('/home')
def home():
    username=session.get('username')
    data_num,top_city,average_salary,hot_jobs=get_Home_Data()
    campany_infos=data_loader.get_datalist_json()[0:4]
    #print(data_num,top_city,average_salary,hot_jobs)
    return render_template('index.html',
                           username=username,
                           data_num=data_num,
                           top_city=top_city,
                           average_salary=average_salary,
                           hot_jobs=hot_jobs,
                           campany_infos=campany_infos
                           )
@pb.route('/datalist')
def data():
    hot_jobs=data_loader.get_datalist_json()
    # hot_jobs = [
    #     ("软件工程师", "北京", "20,000 - 30,000", "全职", "ABC 公司", "https://www.example.com/job1"),
    #     ("数据分析师", "上海", "15,000 - 25,000", "全职", "XYZ 公司", "https://www.example.com/job2"),
    #     ("产品经理", "深圳", "25,000 - 35,000", "全职", "123 公司", "https://www.example.com/job3"),
    #     ("前端开发工程师", "广州", "18,000 - 28,000", "全职", "456 公司", "https://www.example.com/job4"),
    # ]
    return render_template('list.html', hot_jobs=hot_jobs)


    return render_template('list.html',)



@pb.route('/data/<param>',methods=['GET', 'POST'])
@cross_origin()
def data_request(param):
    print(f'请求{param}数据')
    data=data_loader.get_academic_json()
    if param=='job_time':
        data=data_loader.get_jobtime_data()
    if param =='hot_position':#热门岗位占比
        data={'total':1000,'data':[
               { 'value': 1048, 'name': 'Search Engine' },
               { 'value': 735, 'name': 'Direct' },
               { 'value': 580, 'name': 'Email' },
               { 'value': 484, 'name': 'Union Ads' },
               { 'value': 300, 'name': 'Video Ads' }
               ]
               }
    if param =='academic':
        data=data_loader.get_academic_json()
    elif param=='reward':  
        data=data_loader.get_reward_json()
    elif param=='scale':  
        data=data_loader.get_scale_json()
    elif param=='industry':  
            data=data_loader.get_industry_json()
    elif param=='province':  
        data=data_loader.get_province_json()
    elif param=='capacity':  
        data=data_loader.get_capacity_json()
    elif param=='languages':
        data={'total':1000,'data':[
               { 'value': 1048, 'name': 'Search Engine' },
               { 'value': 735, 'name': 'Direct' },
               { 'value': 580, 'name': 'Email' },
               { 'value': 484, 'name': 'Union Ads' },
               { 'value': 300, 'name': 'Video Ads' }
               ]
               
               }
    return jsonify(data)

@pb.route('/woundcloud/<param>',methods=['GET', 'POST'])
@cross_origin()
def woundcloud(param):
    if param =='academic':
        data=data_loader.get_academic_json()
    if param=='reward':  
        data=data_loader.get_reward_json()
    if param=='scale':  
        data=data_loader.get_scale_json()
    if param=='industry':  
            data=data_loader.get_industry_json()
    if param=='province':  
        data=data_loader.get_province_json()
    if param=='capacity':  
        data=data_loader.get_capacity_json()
    hot_jobs = {
            'value':data,
              'image':"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAYAAADDPmHLAAAKO0lEQVR4Xu2dC8weRRWGn0oUEIGCRYsKWBRFLV4QBYOiKFRFripNxXqtICICio0YuYiQgKZYrnIJhoCICgG12CrYqKAWlFivoIj1gihGRQraeFfyfu7+/v36XWZmZ3dnvj0n+dPSf+bMOe+87M7MnnNmBiadRmBGp70352mbAM8EtgPmAI8C7gHuBn4DrJmw+XkMsEPh028LH1t3sQ0CPAF4JzAf2HEMAl8HvgB8FrirdbTcDXg6sA/wEkB/3x7YdEB3+XUt8El31XFbNkmA2cAZwJsDXfgxcAlwMfDXQB11dpsJHA8sArb1HEjkfi+wzLNf5eZNEeBwYAmwRWWL4Y/A+cB5wJ8i6KuqQj69u5j8zSsq+zjwtoo6vLo3QYCzgWO9rHJr/ABwYkEGtx7xW720eHzr6RZL9No7CLg/lsJReuomgB7XR9TsyA+BtwO31DxOv/ozgffVNOZqQOQSyWuVOgkgcARSU6L370cbGOyxwOeB3Wse6zvA3sCf6xynLgIc0MaCBrgAOLpGwHYtdiW+i7xQk1YArwrt7NKvDgIInDsArYrbEG0bRcDYcnCxHY2td5w+LZ4Xj2sU+vs6CPAl4OWhBkXq903glREfn68HroxkW4iafYGVIR3H9YlNgEOBq8cN2tDvvwu8LMJqWvv6SxuyedgwvwaeWsf5R0wC6KTrp4BO+lKRVcCeFYxpay0zyORaXgUxCXAycGoFsOvqehWgR7ivaMGnPfkjfTvW2H4X4Ecx9ccigD50/BzYLKZxEXUdU5wcuqrcGbgZ2Ma1Q0PttLZ5YcyxYhFA26+jYhpWg665wO0OekVmtZvl0LaNJocBn4o1cAwCbA3o8+bGsYwyPSMR0JP2KcC/Y+AUgwBNn/jF8Dt3Hfq4FmVnEoMAv5wW6JA7sLnYr22hYgwqS1UC7Acsr2yFKQhBYGGMQJKqBFBEi45ITZpH4HvAc6oOW4UA2iL9vqoB1r8SAgo5u6mKhioEOA5YWmVw61sZgU8Dr6uipQoBvgU8v8rg1rcyAv8EdG6xNlRTKAF03q+VqEn7CCjc7txQM0IJYHv/UMTj96u0GAwlwG3AbvF9MY2BCDyjCMLx7h5CAB1A/Mp7JOtQJwIfCQ1QDSGA3jkK9TZJB4Hgk8EQAtwIKETJJC0EXlx8wvayypcACo54ENjIaxRr3AQCQRHRvgRIKUSqCVBzGkOnsspZ8BJfAnwMeIfXCNa4SQSUSPI1nwF9CaDFRkpBnz6+dqGtUvGO9HHUhwBPzixH3weHSWmrbGkdDTtHC/kQQDF/WmiYpI2AciG+4mqiDwGUEHmgq2Jr1xoCOqNRvQIncSWAtn1KVU417NvJ2Y40UnKOsoicxJUAyq75hpNGa5QCAqq99AsXQ1wJ8AHgdBeF1iYJBFRv6CwXS1wJkELGr4s/1uZ/CChYZw8XMFwI8LDi/a86fib5IKA6Db8bZ64LAVQK5dZxiuz3ySHwLpcCWi4EUJLki5Jzzwwah8ANwCvGNRpHgLcCql1nkicCqjT21VGmjyLAo4GftVjrJ0/I07JaiaQqVfv3YWaNIsAVwBvS8sesCUDgQ8ApvgRQvL+2EiaTgcDQg6FhT4Drgf0nw3fzoihv9+pBSAwigEKMo9ahsSlIAoGBeYSDCPCZopZ/ElabEdEQ+D7w7H5t/QTYCfgJoNM/k8lDYB7w5elu9RNAxZadvyVPHj4T75G+6aiC6pRMJ4D+rrNjhRSZTC4COhfQ7Ss9mU4AJRZ4RZROLkYT7Zkiu3Vn0wYEuKi4eGGivTfnepFdyh/onQ6WTwCFfP0B2MoA6gQCurjr8ukEsJCvTsz7lJOKGlb08NQTwAo+dIsAyhvQx74HyleAHf12iwDyVh/6riwJoIwSe/93iwQqOH2YCGBn/92a+NJbhY3vKAIsiFl+vJtYZuv1ViJAqjd9ZItqRobPEwF0G1bIlSoZ+WmmDkHgOBHg28DzDKJOInCOCHA3sF0n3TenrxcB7gN07YtJ9xBYLQL8t3t+m8cFAmuMAN3mwn1GgG4ToPcxaF1it2N2fEoadX+dCGC3fjWKeVKD3SsCWOn3pOakUWPuFAFW9EeKNmqCDdYmAreJAAoNemObVtjYrSFwnQhwEqAMUpPuIXCaCKBEAb0GTLqHwAIRYCZwf/d8N4+BXcqQMN0BFOUyYoM1GwR0/rNlSYBrgYH549m4Y4b6IrAMOKgkwDHAOb4arH3WCPTKyJUEeDxwT9bumPG+COwM9A6CSlkFvMBXi7XPEgHVgHiaLJ9OALsNPMu5DDJ6MbCknwCzgXuD1FmnnBD4D6C5VjLwek8A/fdNwF45eWO2eiPwOeCQsld/iZiDi5Ji3lqtQzYIPBdYPYwAIsQaYE427pihPgjoCa9ycVPS/wTQLw4HLvHRam2zQUB3Pq8cR4BHALog0opFZTOvToYuH1T9ddATQNpOAM5wUmuNckHgSYCqh68nwwigRioVr04m+SPw4eJ/6g08GUUALRZGXjaQPy6d8ECnfs8C/jHI21EEUPvLAFWUMskTgX8B2vb9YJj54wigsjFikC0I8yTA+4EzR5k+jgDq+1rgmjz977TVen3rzqCR4kIAKbjQ9176cQPb72tFYG3xtS/KvYGy9OFFAokWEyZpI6AagDrwcVrAuz4B5PITi8XE5mn733nrjgYucEXBhwDSeQCgWDKTNBFYrxK4i4m+BJDOE4HTXJRbm0YRWAq8x3fEEAJoDEWTHO87mLWvDQFt9bTl85ZQAmig8wC9b0zaReCDwKmhJlQhgMa8FFgUOrj1q4zAVGxfqKaqBDAShCJfvZ8yuj9RVU0MAsiGY4Gzqxpj/Z0Q+BtwYP/1b049BzSKRQCp3ge42srOh06FUz/l8wnnW51aOzSKSQANp8OiLwLKOjGJi8DtwGuUzRNTbWwCyLYtipOohTEN7bguvV5rudCzDgKUczW/2CXY0XE4exXC9Rbg5nAVo3vWSQCNrKRTrVT3rsuBCdYr3I4AtOirTeomQGm4jihPBzatzZPJUazq7Zr4G5pwqSkCyJdtisDEo4BNmnAuszFUpkffWfRBpzFpkgClUwovU2UyJaBs3JinaQ90BaDs7MZrNbVBgHIqtD4Q449Me25qtU6RVucDd9Q6ygjlbRKgNEupyrq5VKvdLdsCosFx/wJcDChWv5ei3aakQIDp/h9aEEG1CydN7gLOKi7p0oleEpIaAUpQti3K176pLGWSBFr+RjwIKCfvojr38v5m/b9HqgSY7tPugA6V9FTo1bVJXHRkqzD6G4FbErd1gwohqdur9cJ+wDxgD2CHBAzWQY0mWrn3VwF61GcjOTwBRoGp285EBP3sBsxt4Ao8pc5rwvWjymq6dzFbyZ0Ag4DfrHhV6HWxU0GIxxV/auupj1XDRIkUOn/XVXrak+tHK3X9m7Kl9SVO7/WJkUkkgMvkzCqIIDLoY5UmXJNc67m7i2FNt+kqAZrGOdnxjADJTk0zhhkBmsE52VEeAmv0SlvfFLheAAAAAElFTkSuQmCC"
          }
    return jsonify(hot_jobs)
# @pb.route('/woundcloud',methods=['GET', 'POST'])
# @cross_origin()
# def woundcloud():
#     data=data_loader.get_reward_json()
#     hot_jobs = {
#             'value':data,
#             # 'value': [{
#             #   "name": "五金一险",
#             #   "value": 0
#             # },
#             #   {
#             #     "name": "不熬夜",
#             #     "value": 0
#             #   },
#             #   {
#             #     "name": "不加班",
#             #     "value": 0
#             #   },
#             #   {
#             #     "name": "不早起",
#             #     "value": 0
#             #   },
#             #   {
#             #     "name": "福利多",
#             #     "value": 0
#             #   },
#             #   {
#             #     "name": "薪资高",
#             #     "value": 0
#             #   },
#             #   {
#             #     "name": "活动多",
#             #     "value": 0
#             #   },
#             #   {
#             #     "name": "环境好",
#             #     "value": 0
#             #   },
#             #   {
#             #     "name": "升值快",
#             #     "value": 0
#             #   },
#             #   {
#             #     "name": "有股份",
#             #     "value": 0
#             #   },
#             #   {
#             #     "name": "退休福利好",
#             #     "value": 0
#             #   },
#             #   {
#             #     "name": "牛",
#             #     "value": 0
#             #   },
#             #   {
#             #     "name": "国企",
#             #     "value": 0
#             #   },
#             #   {
#             #     "name": "包吃包住",
#             #     "value": 0
#             #   },
#             # ],
#               'image':"data:image/png;base64,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"
#           }
#     return jsonify(hot_jobs)
@pb.route('/chinamap',methods=['GET', 'POST'])
@cross_origin()
def chinamap():
    #print( type(data_loader.get_province_json()))
    data = data_loader.get_province_json()
    # hot_jobs=[
    #                     {"name": '北京', "value": 0},
    #                     {"name": '天津', "value": 0},
    #                     {"name": '上海', "value": 0},
    #                     {"name": '重庆', "value": 0},
    #                     {"name": '河北', "value": 0},
    #                     {"name": '河南', "value": 0},
    #                     {"name": '云南', "value": 0},
    #                     {"name": '辽宁', "value": 0},
    #                     {"name": '黑龙江', "value": 0},
    #                     {"name": '湖南', "value": 0},
    #                     {"name": '安徽', "value": 0},
    #                     {"name": '山东', "value": 0},
    #                     {"name": '新疆', "value": 0},
    #                     {"name": '江苏', "value": 0},
    #                     {"name": '浙江', "value": 0},
    #                     {"name": '江西', "value": 0},
    #                     {"name": '湖北', "value": 0},
    #                     {"name": '广西', "value": 0},
    #                     {"name": '甘肃', "value": 0},
    #                     {"name": '山西', "value": 0},
    #                     {"name": '内蒙古', "value": 0},
    #                     {"name": '陕西', "value": 0},
    #                     {"name": '吉林', "value": 0},
    #                     {"name": '福建', "value": 0},
    #                     {"name": '贵州', "value": 0},
    #                     {"name": '广东', "value": 0},
    #                     {"name": '青海', "value": 0},
    #                     {"name": '西藏', "value": 0},
    #                     {"name": '四川', "value": 0},
    #                     {"name": '宁夏', "value": 0},
    #                     {"name": '海南', "value": 0},
    #                     {"name": '台湾', "value": 0},
    #                     {"name": '香港', "value": 0},
    #                     {"name": '澳门', "value": 0}
    #                 ]
    # for d in data:
    #   print(d)
    #   for e in hot_jobs:
    #       # print(d,e)
    #       if e['name']==d['name']:
    #           e['value'] = d['value']

    return jsonify(data)




@pb.route('/show')
def show():
    return render_template('base_show.html')
@pb.route('/view')
def view():
    return render_template('view copy.html')
