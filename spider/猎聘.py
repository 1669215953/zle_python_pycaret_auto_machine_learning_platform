import requests

cookies = {
    '__gc_id': '9abb2ded81854310907fe2a0dd9aac92',
    '_ga': 'GA1.1.1457399171.1695213773',
    '__uuid': '1695213773691.69',
    'UniqueKey': 'fc67ab9086a3991740d501f6e766523c',
    'liepin_login_valid': '0',
    'lt_auth': 'vO4OOnIBz1jw5SGM3zAL4v4YiIihAT7L83kFjEoFgoW8DfDr4P%2FnQQuCqrYA9CoIq0wkcq0zMLb3MOr%2FyntL6Eob%2FlGnlpyuvPKk1ngeSudcN8W2vezHl8zRQpQcl0AC8nFbtkIL%2BQ%3D%3D',
    'access_system': 'C',
    'need_bind_tel': 'false',
    'new_user': 'true',
    'c_flag': 'c146b4835afc6d49ce9154d4a912e90a',
    'imId': '1216c9ef38c61d14fea535e52092926d',
    'imId_0': '1216c9ef38c61d14fea535e52092926d',
    'imClientId': '1216c9ef38c61d148cced28bd99be7da',
    'imClientId_0': '1216c9ef38c61d148cced28bd99be7da',
    'inited_user': 'de4f9ea86f3d913bffde7fdc1ac79ff3',
    'user_roles': '0',
    'user_photo': '5f8fa3a8ea60860b75385c7208u.png',
    'user_name': '%E7%8E%8B%E4%BF%8A%E6%B5%A9',
    'XSRF-TOKEN': 'olzQCFIIRiaJ-R_rW-ha3w',
    '__tlog': '1695215842386.25%7C00000000%7C00000000%7Cs_o_007%7Cs_o_007',
    'acw_tc': '276077b816952158521404594e43bb5731327f9044b26c9bbd19355c6476e8',
    'hpo_role-sec_project': 'sec_project_liepin',
    'hpo_sec_tenant': '0',
    'Hm_lvt_a2647413544f5a04f00da7eee0d5e200': '1695213774,1695215843',
    'imApp_0': '1',
    'Hm_lpvt_a2647413544f5a04f00da7eee0d5e200': '1695217451',
    'fe_im_socketSequence_new_0': '3_3_3',
    'fe_im_opened_pages': '1695217367904',
    'fe_im_connectJson_0': '%7B%220_fc67ab9086a3991740d501f6e766523c%22%3A%7B%22socketConnect%22%3A%222%22%2C%22connectDomain%22%3A%22liepin.com%22%7D%7D',
    '_ga_54YTJKWN86': 'GS1.1.1695217624.2.0.1695217624.0.0.0',
    '__session_seq': '4',
    '__uv_seq': '8',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8;',
    # 'Cookie': '__gc_id=9abb2ded81854310907fe2a0dd9aac92; _ga=GA1.1.1457399171.1695213773; __uuid=1695213773691.69; UniqueKey=fc67ab9086a3991740d501f6e766523c; liepin_login_valid=0; lt_auth=vO4OOnIBz1jw5SGM3zAL4v4YiIihAT7L83kFjEoFgoW8DfDr4P%2FnQQuCqrYA9CoIq0wkcq0zMLb3MOr%2FyntL6Eob%2FlGnlpyuvPKk1ngeSudcN8W2vezHl8zRQpQcl0AC8nFbtkIL%2BQ%3D%3D; access_system=C; need_bind_tel=false; new_user=true; c_flag=c146b4835afc6d49ce9154d4a912e90a; imId=1216c9ef38c61d14fea535e52092926d; imId_0=1216c9ef38c61d14fea535e52092926d; imClientId=1216c9ef38c61d148cced28bd99be7da; imClientId_0=1216c9ef38c61d148cced28bd99be7da; inited_user=de4f9ea86f3d913bffde7fdc1ac79ff3; user_roles=0; user_photo=5f8fa3a8ea60860b75385c7208u.png; user_name=%E7%8E%8B%E4%BF%8A%E6%B5%A9; XSRF-TOKEN=olzQCFIIRiaJ-R_rW-ha3w; __tlog=1695215842386.25%7C00000000%7C00000000%7Cs_o_007%7Cs_o_007; acw_tc=276077b816952158521404594e43bb5731327f9044b26c9bbd19355c6476e8; hpo_role-sec_project=sec_project_liepin; hpo_sec_tenant=0; Hm_lvt_a2647413544f5a04f00da7eee0d5e200=1695213774,1695215843; imApp_0=1; Hm_lpvt_a2647413544f5a04f00da7eee0d5e200=1695217451; fe_im_socketSequence_new_0=3_3_3; fe_im_opened_pages=1695217367904; fe_im_connectJson_0=%7B%220_fc67ab9086a3991740d501f6e766523c%22%3A%7B%22socketConnect%22%3A%222%22%2C%22connectDomain%22%3A%22liepin.com%22%7D%7D; _ga_54YTJKWN86=GS1.1.1695217624.2.0.1695217624.0.0.0; __session_seq=4; __uv_seq=8',
    'Origin': 'https://www.liepin.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.liepin.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.31',
    'X-Client-Type': 'web',
    'X-Fscp-Bi-Stat': '{"location": "https://www.liepin.com/zhaopin/?inputFrom=c_index&workYearCode=0&key=%E7%AE%97%E6%B3%95%E5%B7%A5%E7%A8%8B%E5%B8%88&scene=input&ckId=4lrh13dg2qxy4va3bypxp4lvwhfbvgqa&"}',
    'X-Fscp-Fe-Version': '',
    'X-Fscp-Std-Info': '{"client_id": "40108"}',
    'X-Fscp-Trace-Id': 'f196bcdc-0445-49a9-9271-2678fb168a0b',
    'X-Fscp-Version': '1.1',
    'X-Requested-With': 'XMLHttpRequest',
    'X-XSRF-TOKEN': 'olzQCFIIRiaJ-R_rW-ha3w',
    'sec-ch-ua': '"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'data': {
        'mainSearchPcConditionForm': {
            'city': '410',
            'dq': '410',
            'pubTime': '',
            'currentPage': 0,
            'pageSize': 40,
            'key': 'python',
            'suggestTag': '',
            'workYearCode': '0',
            'compId': '',
            'compName': '',
            'compTag': '',
            'industry': '',
            'salary': '',
            'jobKind': '',
            'compScale': '',
            'compKind': '',
            'compStage': '',
            'eduLevel': '',
        },
        'passThroughForm': {
            'scene': 'input',
            'skId': '',
            'fkId': '',
            'ckId': 'n5eg5gbosa5a8ef6cfr1w1xnlauvvmzb',
            'suggest': None,
        },
    },
}

response = requests.post(
    'https://api-c.liepin.com/api/com.liepin.searchfront4c.pc-search-job',
    cookies=cookies,
    headers=headers,
    json=json_data,
)
if response.status_code == 200:
    # 保存响应内容到文件
    with open('lieping.txt', 'w+', encoding='utf-8') as f:
        print(response.text)
        f.write(response.text)
        print("页面保存成功！")
else:
    print("请求失败，无法保存页面。")