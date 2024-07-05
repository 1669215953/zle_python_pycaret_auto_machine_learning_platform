import hmac
from hashlib import sha256
import time
import requests
from urllib.parse import quote
import pandas as pd

# 实现 返回 hmac_sha256 算法
def hmac_sha256(key, value):
    message = value.encode('utf-8')
    return hmac.new(key.encode('utf-8'), message, digestmod=sha256).hexdigest()

# 抓取数据
# 参数为需要搜索的招聘信息内容,页码
def get_data(search,page):
    target = "https://cupid.51job.com"
    # hmac_sha256 密钥
    key = "abfc8f9dcf8c3f3d8aa294ac5f2cf2cc7767e5592590f39c3f503271dd68562b"
    # hmac_sha256 加密信息 时间戳 搜索的关键词
    #'/api/job/search-pc?api_key=51job&timestamp=1698050220&keyword=pyhon%E5%AE%9E%E4%B9%A0&searchType=2&function=&industry=&jobArea=040000&jobArea2=&landmark=&metro=&salary=&workYear=&degree=&companyType=&companySize=&jobType=&issueDate=&sortType=0&pageNum=1&requestId=&pageSize=20&source=1&accountId=&pageCode=sou%7Csou%7Csoulb'
    value = f"/api/job/search-pc?api_key=51job&timestamp={str(int(time.time()))}&keyword={search}&searchType=2&function=&industry=&jobArea=040000&jobArea2=&landmark=&metro=&salary=&workYear=&degree=&companyType=&companySize=&jobType=&issueDate=&sortType=0&pageNum={page}&requestId=&pageSize=50&source=1&accountId=235006265&pageCode=sou%7Csou%7Csoulb"
    test=f'/api/job/search-pc?api_key=51job&timestamp={str(int(time.time()))}&keyword=&searchType=2&function=&industry=&jobArea=040000&jobArea2=&landmark=&metro=&salary=&workYear=&degree=&companyType=&companySize=&jobType=&issueDate=&sortType=0&pageNum=1&requestId=&pageSize=20&source=1&accountId=235006265&pageCode=sou%7Csou%7Csoulb'

    # 请求头
    headers = {
        'uuid': '30e54a7135e3545b8c797aef656cf4ce', 
        'user-token': "94df1d379c77552112992ae52eccee706536326b",
        'From-Domain': '51job_web',
        "accountid":"235006265",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61',
        'partner': 'cn_bing_com',
        'property': '%7B%22partner%22%3A%22cn_bing_com%22%2C%22webId%22%3A2%2C%22fromdomain%22%3A%2251job_web%22%2C%22frompageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2F%22%2C%22pageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2Fpc%2Fsearch%3FjobArea%3D040000%22%2C%22identityType%22%3A%22%E8%81%8C%E5%9C%BA%E4%BA%BA%22%2C%22userType%22%3A%22%E8%80%81%E7%94%A8%E6%88%B7%22%2C%22isLogin%22%3A%22%E6%98%AF%22%2C%22accountid%22%3A%22235006265%22%2C%22keywordType%22%3A%22%22%7D'
    }
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'From-Domain': '51job_web',
    'LANGUAGE': '',
    'Origin': 'https://we.51job.com',
    'Pragma': 'no-cache',
    'Referer': 'https://we.51job.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61',
    'account-id': '235006265',
    'partner': 'cn_bing_com',
    'property': '%7B%22partner%22%3A%22cn_bing_com%22%2C%22webId%22%3A2%2C%22fromdomain%22%3A%2251job_web%22%2C%22frompageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2F%22%2C%22pageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2Fpc%2Fsearch%3FjobArea%3D040000%22%2C%22identityType%22%3A%22%E8%81%8C%E5%9C%BA%E4%BA%BA%22%2C%22userType%22%3A%22%E8%80%81%E7%94%A8%E6%88%B7%22%2C%22isLogin%22%3A%22%E6%98%AF%22%2C%22accountid%22%3A%22235006265%22%7D',
    'sec-ch-ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    "sign": hmac_sha256(key, value),
    'user-token': '94df1d379c77552112992ae52eccee706536326b',
    'uuid': '30e54a7135e3545b8c797aef656cf4ce',
}
    cookies = {
    'guid': '30e54a7135e3545b8c797aef656cf4ce',
    'nsearch': 'jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D',
    'partner': 'cn_bing_com',
    'seo_refer_info_2023': '%7B%22referUrl%22%3A%22https%3A%5C%2F%5C%2Fcn.bing.com%5C%2F%22%2C%22referHost%22%3A%22cn.bing.com%22%2C%22landUrl%22%3A%22%5C%2F%22%2C%22landHost%22%3A%22www.51job.com%22%2C%22partner%22%3Anull%7D',
    'privacy': '1698046201',
    'acw_sc__v2': '65362bdf28f02c4570a4971dea00e375c13baf76',
    'acw_tc': 'ac11000116980500024204608e00db70c29dd8063f0113ceffd45dc6eb03ed',
    'Hm_lvt_1370a11171bd6f2d9b1fe98951541941': '1696380367,1698046205,1698050142',
    'Hm_lpvt_1370a11171bd6f2d9b1fe98951541941': '1698050142',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2230e54a7135e3545b8c797aef656cf4ce%22%2C%22first_id%22%3A%2218aa8307aa77bd-0f15a1bf3eb7df-78505774-1327104-18aa8307aa81807%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcn.bing.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThhYTgzMDdhYTc3YmQtMGYxNWExYmYzZWI3ZGYtNzg1MDU3NzQtMTMyNzEwNC0xOGFhODMwN2FhODE4MDciLCIkaWRlbnRpdHlfbG9naW5faWQiOiIzMGU1NGE3MTM1ZTM1NDViOGM3OTdhZWY2NTZjZjRjZSJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2230e54a7135e3545b8c797aef656cf4ce%22%7D%2C%22%24device_id%22%3A%2218aa8307aa77bd-0f15a1bf3eb7df-78505774-1327104-18aa8307aa81807%22%7D',
    'search': 'jobarea%7E%60040000%7C%21recentSearch0%7E%60040000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApyhon%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60040000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApyhon%CA%B5%CF%B0%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch2%7E%60040000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch3%7E%60040000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch4%7E%60040000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApython%CA%B5%CF%B0%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21',
    'JSESSIONID': '440CE1A61F8E2B28651237692E244514',
    'ssxmod_itna2': 'Qq+OiKYvxUxjxWT4BPGKRmBbDCD0DgrW2WgBQg0QDnKdqw5Ds1aDLQS7upj3qn4qC9fDmu0+Vb7uqrGStBly2IizRn9xG4o7uSN1=TzTQiY75DmjnupV=DMy9bhyQZXcsLkM//XL5qLD6kLBU+i0QWonQbiGFR=4Sf3GYAEYw4r4RWfr0+w3HMt=0bLslWu0lfbaTRD5N6c3vkWVfmTH2ZF7ymyoMmurXCcEB1BmAbfmrK9pkn=hCkEUKW3A7qocGPtfx8XmBUuNLmHjGhlI7iIhx6EU9C1xdfET2OD5+X/+/1V2EN3BZdBrXUCD4YwsEt4Se/=qxRh37puepdG0kiGw7pkCInDvkAPdhwy=q10rOCwb+0IAwnjeWfbkYei3KvAw=3qtSmNR5CR5vl6z45o+eFDG27DNbDQynq02P+ObrBMtDQC8HtxQwBPhDHiGbperGDDh0rbDxD08DijOY+tmK4W+nY4YQGZODLD+bladEPNjxeSGgOii3o9Ux5YD',
    'ssxmod_itna': 'YqUxn7itK7q1DXQG7GTF4GqDKi=Mh=GOSQSjjDBkSeiNDnD8x7YDvG+=BG45/RYmSwYd1e2YaKKKFEdT34kzUocKziDCPGnDBIAxF7DxiicDCeDIDWeDiDGR7D=xGYDj0F/C9Dm4i7DYqGRDB=UCqDf+qGW7uQDmLNDGMP6D7QDIM6=DDX=lCwdeoqKvTd5qjbDATmgI749D0UdxBLtI1q9+mFkyBUg7caPT2jx5eGuDG6DOqGmBfbDCg6lWm5IK0DYj8GQGAwaeO+QF7mpjDhezYxHPw+Qealnof4LAHD==',
}
    print("sign:",headers['sign'],str(int(time.time())))
    # 获取响应 json 格式化
    response = requests.get(url=target+value,headers=headers,verify=False)
    print(response.text)
    print(response.text,response.json())
    return response

# 生成csv
# 参数 csv文件名,csv数据
def generate_csv(file_name,data):
    csv_data = pd.DataFrame(data)
    csv_data.to_csv(f"./{file_name}.csv")

def main():
    #岗位
    search_word = "python实习生"
    # 最后的csv的数据
    result = list()
    # 对关键词进行url编码 否则无法实现中文爬虫
    # 翻页
    for page in range(1,10):
        job_data = get_data(search=quote(search_word), page=page)["resultbody"]['job']["items"]
        print(f"[Success] Crawler Page:{page} | OVER",)
        result += job_data
    # 生成csv
    generate_csv(file_name=search_word, data=result)
    print(f"[Success] Generate-Csv {search_word}.csv | OVER")

if __name__ == "__main__":
    main()