import requests
import hmac
from hashlib import sha256
import time
from urllib.parse import quote
import pandas as pd
keyword=input("搜索关键字")
page=input("page")
def hmac_sha256(key, value):
    message = value.encode('utf-8')
    return hmac.new(key.encode('utf-8'), message, digestmod=sha256).hexdigest()
key = "abfc8f9dcf8c3f3d8aa294ac5f2cf2cc7767e5592590f39c3f503271dd68562b"
value = f"/api/job/search-pc?api_key=51job&timestamp={str(int(time.time()))}&keyword={keyword}&searchType=2&function=&industry=&jobArea=000000&jobArea2=&landmark=&metro=&salary=&workYear=&degree=&companyType=&companySize=&jobType=&issueDate=&sortType=0&pageNum={page}&requestId=&pageSize=50&source=1&accountId=&pageCode=sou%7Csou%7Csoulb"

cookies = {
    'guid': '30e54a7135e3545b8c797aef656cf4ce',
    'nsearch': 'jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D',
    'partner': 'cn_bing_com',
    'seo_refer_info_2023': '%7B%22referUrl%22%3A%22https%3A%5C%2F%5C%2Fcn.bing.com%5C%2F%22%2C%22referHost%22%3A%22cn.bing.com%22%2C%22landUrl%22%3A%22%5C%2F%22%2C%22landHost%22%3A%22www.51job.com%22%2C%22partner%22%3Anull%7D',
    'privacy': '1698046201',
    'Hm_lvt_1370a11171bd6f2d9b1fe98951541941': '1696380367,1698046205,1698050142',
    'ps': 'needv%3D0',
    '51job': 'cuid%3D235006265%26%7C%26cusername%3Dgi86yPJyZgdSrkQZ948gBBNrTzAQL9xkCFWvDZq9Xew%253D%26%7C%26cpassword%3D%26%7C%26cname%3D%26%7C%26cemail%3D%26%7C%26cemailstatus%3D0%26%7C%26cnickname%3D%26%7C%26ccry%3D.0Wvy1Y.oofhI%26%7C%26cconfirmkey%3D%25241%25247Knb9aLs%2524V6UkSOlEK6k3eNW4eKH8R0%26%7C%26cautologin%3D1%26%7C%26cenglish%3D0%26%7C%26sex%3D%26%7C%26cnamekey%3D%25241%2524Eyig3xm1%2524ARWf9kfpwduXDFn7zGB%252FI.%26%7C%26to%3D94df1d379c77552112992ae52eccee706536326b%26%7C%26',
    'sensor': 'createDate%3D2023-10-04%26%7C%26identityType%3D1',
    'slife': 'lowbrowser%3Dnot%26%7C%26lastlogindate%3D20231023%26%7C%26securetime%3DDDBTZlA%252FVjpRMwY9X2QKZ1ZjBjg%253D',
    'acw_tc': 'ac11000116980518706763217e00df538e7708226cac40e1231db26e405e81',
    'acw_sc__v2': '6536371e6274ca8fd3f4d6ab09fea707cb29ab73',
    'Hm_lpvt_1370a11171bd6f2d9b1fe98951541941': '1698052152',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22235006265%22%2C%22first_id%22%3A%2218aa8307aa77bd-0f15a1bf3eb7df-78505774-1327104-18aa8307aa81807%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcn.bing.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThhYTgzMDdhYTc3YmQtMGYxNWExYmYzZWI3ZGYtNzg1MDU3NzQtMTMyNzEwNC0xOGFhODMwN2FhODE4MDciLCIkaWRlbnRpdHlfbG9naW5faWQiOiIyMzUwMDYyNjUifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22235006265%22%7D%2C%22%24device_id%22%3A%2218aa8307aa77bd-0f15a1bf3eb7df-78505774-1327104-18aa8307aa81807%22%7D',
    'search': 'jobarea%7E%60040000%7C%21recentSearch0%7E%60040000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60040000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch2%7E%60040000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApyhon%CA%B5%CF%B0%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch3%7E%60040000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApyhon%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch4%7E%60040000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApython%CA%B5%CF%B0%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21',
    'JSESSIONID': 'DEA4A00AA77B9A9E52E46709DE8109CE',
    'ssxmod_itna': 'Qq+xg7nD9idCq0dD=mAuD0xDqAKGQs5NqqrIeDlrnPxA5D8D6DQeGTrRTCrsks19mgrfGAS0YaIPTF6dTf54T6h8XYDU4i8DCk0vdd+DYYkDt4DTD34DYDiOQGIDieDF7dstkDbxYQDmxiODlKHUxDa2xi3jOKDRc5D0xwFDQKDuZ9KDGyKzUhqqmxwuEpwxFoDn=0CeiDkD7ypDla5uUxkrbL6kCyCjSf+E79Gq40OD0FGjxibCaoDUlFz39TTsQreknTKrn23PmhxTjxqOT0eT70qNmGqWiiK+KVSAAZP8qDWG6=x4D===',
    'ssxmod_itna2': 'Qq+xg7nD9idCq0dD=mAuD0xDqAKGQs5NqqrqD6ht=6D0HI2K035njX1usupdADKkwdDLxij=4D==',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'guid=30e54a7135e3545b8c797aef656cf4ce; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; partner=cn_bing_com; seo_refer_info_2023=%7B%22referUrl%22%3A%22https%3A%5C%2F%5C%2Fcn.bing.com%5C%2F%22%2C%22referHost%22%3A%22cn.bing.com%22%2C%22landUrl%22%3A%22%5C%2F%22%2C%22landHost%22%3A%22www.51job.com%22%2C%22partner%22%3Anull%7D; privacy=1698046201; Hm_lvt_1370a11171bd6f2d9b1fe98951541941=1696380367,1698046205,1698050142; ps=needv%3D0; 51job=cuid%3D235006265%26%7C%26cusername%3Dgi86yPJyZgdSrkQZ948gBBNrTzAQL9xkCFWvDZq9Xew%253D%26%7C%26cpassword%3D%26%7C%26cname%3D%26%7C%26cemail%3D%26%7C%26cemailstatus%3D0%26%7C%26cnickname%3D%26%7C%26ccry%3D.0Wvy1Y.oofhI%26%7C%26cconfirmkey%3D%25241%25247Knb9aLs%2524V6UkSOlEK6k3eNW4eKH8R0%26%7C%26cautologin%3D1%26%7C%26cenglish%3D0%26%7C%26sex%3D%26%7C%26cnamekey%3D%25241%2524Eyig3xm1%2524ARWf9kfpwduXDFn7zGB%252FI.%26%7C%26to%3D94df1d379c77552112992ae52eccee706536326b%26%7C%26; sensor=createDate%3D2023-10-04%26%7C%26identityType%3D1; slife=lowbrowser%3Dnot%26%7C%26lastlogindate%3D20231023%26%7C%26securetime%3DDDBTZlA%252FVjpRMwY9X2QKZ1ZjBjg%253D; acw_tc=ac11000116980518706763217e00df538e7708226cac40e1231db26e405e81; acw_sc__v2=6536371e6274ca8fd3f4d6ab09fea707cb29ab73; Hm_lpvt_1370a11171bd6f2d9b1fe98951541941=1698052152; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22235006265%22%2C%22first_id%22%3A%2218aa8307aa77bd-0f15a1bf3eb7df-78505774-1327104-18aa8307aa81807%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcn.bing.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThhYTgzMDdhYTc3YmQtMGYxNWExYmYzZWI3ZGYtNzg1MDU3NzQtMTMyNzEwNC0xOGFhODMwN2FhODE4MDciLCIkaWRlbnRpdHlfbG9naW5faWQiOiIyMzUwMDYyNjUifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22235006265%22%7D%2C%22%24device_id%22%3A%2218aa8307aa77bd-0f15a1bf3eb7df-78505774-1327104-18aa8307aa81807%22%7D; search=jobarea%7E%60040000%7C%21recentSearch0%7E%60040000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60040000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch2%7E%60040000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApyhon%CA%B5%CF%B0%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch3%7E%60040000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApyhon%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch4%7E%60040000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApython%CA%B5%CF%B0%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21; JSESSIONID=07E1FE3BA80343C50896313AF9A3C350; ssxmod_itna=Qq+xg7nD9idCq0dD=mAuD0xDqAKGQs5NqqrIeDlrnPxA5D8D6DQeGTrRTCrsks19mgrfGAS0YaIPTF6dTf54T6h8XYDU4i8DCk0vdd+DYYkDt4DTD34DYDiOQGIDieDF7dstkDbxYQDmxiODlKHUxDa2xi3jOKDRc5D0xwFDQKDuZ9KDGyKzUhqqmxwuEpwxFoDn=0CeiDkD7ypDla5uUxkrbL6kCyCjSf+E79Gq40OD0FGjxibCaoDUlFz39TTsQreknTKrn23PmhxTjxqOT0eT70qNmGqWiiK+KVSAAZP8qDWG6=x4D===; ssxmod_itna2=Qq+xg7nD9idCq0dD=mAuD0xDqAKGQs5NqqrqD6ht=6D0HI2K035njX1usupdADKkwdDLxij=4D==',
    'From-Domain': '51job_web',
    'Pragma': 'no-cache',
    'Referer': 'https://we.51job.com/pc/search?jobArea=040000&keyword=python&searchType=2&sortType=0&metro=',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61',
    'account-id': '235006265',
    'partner': 'cn_bing_com',
    'property': '%7B%22partner%22%3A%22cn_bing_com%22%2C%22webId%22%3A2%2C%22fromdomain%22%3A%2251job_web%22%2C%22frompageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2F%22%2C%22pageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2Fpc%2Fsearch%3FjobArea%3D040000%26keyword%3Dpython%26searchType%3D2%26sortType%3D0%26metro%3D%22%2C%22identityType%22%3A%22%E8%81%8C%E5%9C%BA%E4%BA%BA%22%2C%22userType%22%3A%22%E8%80%81%E7%94%A8%E6%88%B7%22%2C%22isLogin%22%3A%22%E6%98%AF%22%2C%22accountid%22%3A%22235006265%22%2C%22keywordType%22%3A%22%22%7D',
    'sec-ch-ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sign': f'{hmac_sha256(key,value)}',
    'user-token': '94df1d379c77552112992ae52eccee706536326b',
    'uuid': '30e54a7135e3545b8c797aef656cf4ce',
}

params = {
    'api_key': '51job',
    'timestamp': f'{str(int(time.time()))}',
    'keyword': 'python',
    'searchType': '2',
    'function': '',
    'industry': '',
    'jobArea': '040000',
    'jobArea2': '',
    'landmark': '',
    'metro': '',
    'salary': '',
    'workYear': '',
    'degree': '',
    'companyType': '',
    'companySize': '',
    'jobType': '',
    'issueDate': '',
    'sortType': '0',
    'pageNum': '1',
    'requestId': '',
    'pageSize': '20',
    'source': '1',
    'accountId': '235006265',
    'pageCode': 'sou|sou|soulb',
}

response = requests.get('https://we.51job.com/api/job/search-pc', params=params, cookies=cookies, headers=headers,verify=False)
print(response.text)
 

