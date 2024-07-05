from utils.sql import get_all_data,get_job_reward
import re


all_jobs=get_all_data()
rewards=get_job_reward()
def get_data_num():
    '''
    获得岗位数据量
    '''
    return len(all_jobs)


def get_top_city():
    '''
    Index(['职位名称', '地区', '薪水', '标签', '能力要求', '公司名字', '公司介绍', '福利待遇', '职位描述',
       '企业类型', '工作地址', '详情链接'],
      dtype='object')
    
    '''
    column_data = all_jobs['地区']
    citys=column_data.dropna().tolist()
    cities = [address.split('·')[0] for address in citys]
    print(cities)
    city_range={}
    for city in cities:
        city_range[city]=cities.count(city)
    list_count = sorted(city_range.items(), key=lambda x: x[1], reverse=True)
    return list_count[0][0] #('广州', 43)


def get_average_salary():
    '''
    获得平均薪资 
    '''
    column_data = all_jobs['薪水']
    salarys=column_data.dropna().tolist()
    Salary=[]
    for salary in salarys:
        print(salary)
        print(re.findall(r'\d+', salary))
        salary_min, salary_max = re.findall(r'(\d+)', salary)[0:2]
        print(salary_min,salary_max)
        if '天' in salary:
            salary_min = int(salary_min)*30
            salary_max = int(salary_max)*30
        elif 'K' in salary:
            salary_min = int(salary_min)*1000
            salary_max = int(salary_max)*1000
        Salary.append((salary_min,salary_max))
        total_min = sum([int(x[0]) for x in Salary])
        total_max = sum([int(x[1]) for x in Salary])
        average_salary_min = int(total_min / len(Salary))
        average_salary_max = int(total_max / len(Salary))        
    return average_salary_min,average_salary_max
def get_popular_jobs( n=10):
    '''
    根据数据库中的职业名称得出热门岗位
    '''
    column_data = all_jobs['职位名称']
    job_counts = column_data.value_counts()
    
    # 获取出现频次最高的职业名称
    popular_jobs = job_counts.index.tolist()[:n]  # 获取前10个热门岗位
    print("热门岗位:",job_counts[:n].to_dict())
    return job_counts[:n].to_dict()

def get_Home_Data(n=4):
    data_num=get_data_num()
    top_city=get_top_city()
    average_salary=get_average_salary()
    hot_jobs=get_popular_jobs(n)
    """
    data_num  int
    top_city  string
    average_salary  (min,max)
    hot_jobs list
    """
    return data_num,top_city,average_salary,hot_jobs

if __name__=='__main__':
    #print(type(all_jobs))
    #print(get_top_city())
    print(get_average_salary())
    get_popular_jobs()