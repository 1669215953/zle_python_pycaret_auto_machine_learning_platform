import requests
import hmac
from hashlib import sha256
import time
from urllib.parse import quote
import pandas as pd
#keyword=input("搜索关键字")
page=1#input("page")
target = "https://we.51job.com"

def hmac_sha256(key, value):
    message = value.encode('utf-8')
    return hmac.new(key.encode('utf-8'), message, digestmod=sha256).hexdigest()

value=f'/api/job/search-pc?api_key=51job&timestamp={str(int(time.time()))}&keyword=123&searchType=2&function=&industry=&jobArea=040000%2C010000%2C020000%2C030200%2C180200&jobArea2=&landmark=&metro=&salary=&workYear=&degree=&companyType=&companySize=&jobType=&issueDate=&sortType=0&pageNum=1&requestId=&pageSize=20&source=1&accountId=235006265&pageCode=sou%7Csou%7Csoulb'
key = "abfc8f9dcf8c3f3d8aa294ac5f2cf2cc7767e5592590f39c3f503271dd68562b"
#print(value)
#value=f'/api/job/search-pc?api_key=51job&timestamp={str(int(time.time()))}&keyword=python&searchType=2&function=&industry=&jobArea=040000%2C010000%2C020000%2C030200%2C180200&jobArea2=&landmark=&metro=&salary=&workYear=&degree=&companyType=&companySize=&jobType=&issueDate=&sortType=0&pageNum=1&requestId=&pageSize=20&source=1&accountId=235006265&pageCode=sou%7Csou%7Csoulb'
#print(value)
#value = f"/api/job/search-pc?api_key=51job&timestamp={str(int(time.time()))}&keyword={keyword}&searchType=2&function=&industry=&jobArea=000000&jobArea2=&landmark=&metro=&salary=&workYear=&degree=&companyType=&companySize=&jobType=&issueDate=&sortType=0&pageNum={page}&requestId=&pageSize=50&source=1&accountId=&pageCode=sou%7Csou%7Csoulb"
#value=f'/api/job/search-pc?api_key=51job&timestamp={str(int(time.time()))}&keyword={keyword}&searchType=2&function=&industry=&jobArea=040000&jobArea2=&landmark=&metro=&salary=&workYear=&degree=&companyType=&companySize=&jobType=&issueDate=&sortType=0&pageNum={page}&requestId=&pageSize=20&source=1&accountId=235006265&pageCode=sou%7Csou%7Csoulb'

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'guid=30e54a7135e3545b8c797aef656cf4ce; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; ps=needv%3D0; 51job=cuid%3D235006265%26%7C%26cusername%3Dgi86yPJyZgdSrkQZ948gBBNrTzAQL9xkCFWvDZq9Xew%253D%26%7C%26cpassword%3D%26%7C%26cname%3D%26%7C%26cemail%3D%26%7C%26cemailstatus%3D0%26%7C%26cnickname%3D%26%7C%26ccry%3D.0Wvy1Y.oofhI%26%7C%26cconfirmkey%3D%25241%25247Knb9aLs%2524V6UkSOlEK6k3eNW4eKH8R0%26%7C%26cautologin%3D1%26%7C%26cenglish%3D0%26%7C%26sex%3D%26%7C%26cnamekey%3D%25241%2524Eyig3xm1%2524ARWf9kfpwduXDFn7zGB%252FI.%26%7C%26to%3D94df1d379c77552112992ae52eccee706536326b%26%7C%26; sensor=createDate%3D2023-10-04%26%7C%26identityType%3D1; partner=cn_bing_com; seo_refer_info_2023=%7B%22referUrl%22%3A%22https%3A%5C%2F%5C%2Fcn.bing.com%5C%2F%22%2C%22referHost%22%3A%22cn.bing.com%22%2C%22landUrl%22%3A%22%5C%2F%22%2C%22landHost%22%3A%22www.51job.com%22%2C%22partner%22%3Anull%7D; privacy=1698195339; Hm_lvt_1370a11171bd6f2d9b1fe98951541941=1698046205,1698050142,1698159413,1698195341; Hm_lpvt_1370a11171bd6f2d9b1fe98951541941=1698195341; acw_tc=ac11000116981953667115068e00d24d270546763921f5c2f9ad05f073e1a3; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22235006265%22%2C%22first_id%22%3A%2218aa8307aa77bd-0f15a1bf3eb7df-78505774-1327104-18aa8307aa81807%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcn.bing.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThhYTgzMDdhYTc3YmQtMGYxNWExYmYzZWI3ZGYtNzg1MDU3NzQtMTMyNzEwNC0xOGFhODMwN2FhODE4MDciLCIkaWRlbnRpdHlfbG9naW5faWQiOiIyMzUwMDYyNjUifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22235006265%22%7D%2C%22%24device_id%22%3A%2218aa8307aa77bd-0f15a1bf3eb7df-78505774-1327104-18aa8307aa81807%22%7D; slife=lastlogindate%3D20231025%26%7C%26securetime%3DADxVYFg3AGwCYQUyAT8PZ1diV2c%253D; acw_sc__v2=653867a8e78a364e5c8794d9e4e3e4135bf69089; search=jobarea%7E%60040000%2C010000%2C020000%2C030200%2C180200%7C%21recentSearch0%7E%60040000%2C010000%2C020000%2C030200%2C180200%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA123%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60040000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch2%7E%60040000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch3%7E%60040000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%C5%C0%B3%E6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch4%7E%60040000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FAweb%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21; JSESSIONID=BF12A630CC89BEE4673EF68ECFAADF39; ssxmod_itna=iqmx0D9D2Qi=fhDl8Am3eY5DtfCq7Ke=4e3GkQaDBTEr4iNDnD8x7YDvmA59QmtiAhh=vF=enpiYF6x2GFZ9jSe2aKU4W4GLDmKDyD=xweDxhq0rD74irDDxD3pxneD+D0+kSc1qi3DhxDODWKDXZPCDicCDm+kAxGCVxDCRnPDwx0C2ODDBODAKGxYkB711xgGH4D1GWv43BKD9poDsci6KB9m9+LxgavL0RB3Aa7hDCKDj=AkDmnHH4Gd265wDxPxqY2Nejhe=n4Y3jrKq7GYku0DOCRoODLoajxEmyzbFlT/DDPeFDdiYGDD=; ssxmod_itna2=iqmx0D9D2Qi=fhDl8Am3eY5DtfCq7Ke=4e3GkiD8TZExGXT0xGa7QAyQKtsx8oq=s3A=B54he=SMmiiPVcCYWskCba3xfYZEPIXKoExSHBUWs+kO6uLPXlgnp82ZaLlsyob/jSse2MjDoRXE3Q=fAq=8tmrffEiYHjUsmmX08Qb5H4u5ylANZxo=djTB4ar4/x2T2xhaqaRg+craO3WesPj8dqH8cWdynWEzo95FLnKfYCb8jur/nR7Pv6iIHSSVAo76692=SIK1o+YkpzOpv1S6Tm1yBz3BLgETHVEXfON7H5/vFvAXBX2A=Bp=qhtwp=CijPIwllEKfDahwSQ28cwqzD7GwEGG=A4DQKxKDYQ0dWigmA=Dhn92oauKlyDfrqRGfiOr9i77i=9iKzEuYGa00l7goxYx44r6hxD5e34YK8qiRDQi4t3Wp3b9iNz3ok+48i7Yi30SH6h7ErOZ3YDk8HLb8d8ygtD08DiQPl+1C+KQ2KBbqD4ZUwHEDRmDw+boUHrYwT+GkbBqCuTBWT9W0OGTCTilTWbIqqqWUH2zbs3D',
    'From-Domain': '51job_web',
    'Pragma': 'no-cache',
    'Referer': 'https://we.51job.com/pc/search?jobArea=040000,010000,020000,030200,180200&keyword=123&searchType=2&sortType=0&metro=',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61',
    'account-id': '235006265',
    'partner': 'cn_bing_com',
    'property': '%7B%22partner%22%3A%22cn_bing_com%22%2C%22webId%22%3A2%2C%22fromdomain%22%3A%2251job_web%22%2C%22frompageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2F%22%2C%22pageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2Fpc%2Fsearch%3FjobArea%3D040000%2C010000%2C020000%2C030200%2C180200%26keyword%3D123%26searchType%3D2%26sortType%3D0%26metro%3D%22%2C%22identityType%22%3A%22%E8%81%8C%E5%9C%BA%E4%BA%BA%22%2C%22userType%22%3A%22%E8%80%81%E7%94%A8%E6%88%B7%22%2C%22isLogin%22%3A%22%E6%98%AF%22%2C%22accountid%22%3A%22235006265%22%2C%22keywordType%22%3A%22%E7%9B%B4%E6%8E%A5%E8%BE%93%E5%85%A5%22%7D',
    'sec-ch-ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sign': f'{hmac_sha256(key, value)}',
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
    'jobArea': '040000,010000,020000,030200,180200',
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
response = requests.get(target,params=params ,headers=headers)#,verify=False)
print(response.status_code, response.text)
with open("test.txt",'w',encoding='utf-8') as f:
    f.write(response.text)

