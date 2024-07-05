import requests
import json
import csv
def school(key='算法工程师'):
    cookies = {
        'NOWCODERUID': '186A76E083F10CADEEFE2B95950E7B24',
        'NOWCODERCLINETID': '66EC9833B0A846AD902AE0887564D796',
        'gr_user_id': '1fa5bb6c-c77e-4b7c-9122-51e609c614d7',
        '_bl_uid': '2wl4th8mchXyjgrOhutXupb6Uh5w',
        'c196c3667d214851b11233f5c17f99d5_gr_last_sent_cs1': '261863240',
        'YD00000586307807%3AWM_TID': 'elQRobNlZhlBVUUUQFaAKqogiGhtmj9E',
        'YD00000586307807%3AWM_NI': 'vBoX3ciBWTDhKLifhEAxG%2FO0sbOjpd9bVI3528M%2FPSD4PUwTt5idqtYASO0mJJ%2FrBnE92He183N8JYgUuwuwb6BIrNXpN31sj04WpMmP5ZwL725bHzm3hxhqnfAE33sBZVc%3D',
        'YD00000586307807%3AWM_NIKE': '9ca17ae2e6ffcda170e2e6eebbe45b958bbc85ef3a85eb8ea2d55a879f8e86c874928abed3cf6eb0b5e1d8d92af0fea7c3b92ab69ea1b9b269ab9e99b5c7648994a787eb4f83a889d0ce3cb1be818bf370fbbe9aaab23ff2e883d0d35988eca0b6f660b8eba785f4809b9f9db0b3678a96e193c16687e7fea9e83bfced82d9c953a58bbb98f87da2ea8eaaf1469cb082d4b479aaf0fcb8f347af90fbbbf648f5eefb83cb72afeda899eb7baeba8fa6b239b19e96b7e237e2a3',
        'acw_tc': 'bdf0fb3869e27413df60dfb0a3013eeb4f37171723271caf1de3c0cce5b0de7b',
        'csrfToken': '_RzhvYbLjpvtdOx7hIN_o2gO',
        'Hm_lvt_a808a1326b6c06c437de769d1b85b870': '1692880486,1695103766,1695107008',
        'c196c3667d214851b11233f5c17f99d5_gr_session_id': '36043343-941c-49b1-ac67-509c9e7be7cf',
        'c196c3667d214851b11233f5c17f99d5_gr_session_id_36043343-941c-49b1-ac67-509c9e7be7cf': 'true',
        'SERVERID': '4500890894435736ae70a9add3498842|1695108468|1695107014',
        'SERVERCORSID': '4500890894435736ae70a9add3498842|1695108468|1695107014',
        'Hm_lpvt_a808a1326b6c06c437de769d1b85b870': '1695108461',
    }

    headers = {
        'authority': 'www.nowcoder.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'NOWCODERUID=186A76E083F10CADEEFE2B95950E7B24; NOWCODERCLINETID=66EC9833B0A846AD902AE0887564D796; gr_user_id=1fa5bb6c-c77e-4b7c-9122-51e609c614d7; _bl_uid=2wl4th8mchXyjgrOhutXupb6Uh5w; c196c3667d214851b11233f5c17f99d5_gr_last_sent_cs1=261863240; YD00000586307807%3AWM_TID=elQRobNlZhlBVUUUQFaAKqogiGhtmj9E; YD00000586307807%3AWM_NI=vBoX3ciBWTDhKLifhEAxG%2FO0sbOjpd9bVI3528M%2FPSD4PUwTt5idqtYASO0mJJ%2FrBnE92He183N8JYgUuwuwb6BIrNXpN31sj04WpMmP5ZwL725bHzm3hxhqnfAE33sBZVc%3D; YD00000586307807%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eebbe45b958bbc85ef3a85eb8ea2d55a879f8e86c874928abed3cf6eb0b5e1d8d92af0fea7c3b92ab69ea1b9b269ab9e99b5c7648994a787eb4f83a889d0ce3cb1be818bf370fbbe9aaab23ff2e883d0d35988eca0b6f660b8eba785f4809b9f9db0b3678a96e193c16687e7fea9e83bfced82d9c953a58bbb98f87da2ea8eaaf1469cb082d4b479aaf0fcb8f347af90fbbbf648f5eefb83cb72afeda899eb7baeba8fa6b239b19e96b7e237e2a3; acw_tc=bdf0fb3869e27413df60dfb0a3013eeb4f37171723271caf1de3c0cce5b0de7b; csrfToken=_RzhvYbLjpvtdOx7hIN_o2gO; Hm_lvt_a808a1326b6c06c437de769d1b85b870=1692880486,1695103766,1695107008; c196c3667d214851b11233f5c17f99d5_gr_session_id=36043343-941c-49b1-ac67-509c9e7be7cf; c196c3667d214851b11233f5c17f99d5_gr_session_id_36043343-941c-49b1-ac67-509c9e7be7cf=true; SERVERID=4500890894435736ae70a9add3498842|1695108468|1695107014; SERVERCORSID=4500890894435736ae70a9add3498842|1695108468|1695107014; Hm_lpvt_a808a1326b6c06c437de769d1b85b870=1695108461',
        'origin': 'https://www.nowcoder.com',
        'pragma': 'no-cache',
        'referer': 'https://www.nowcoder.com/jobs/fulltime/center?recruitType=3&search=%E7%AE%97%E6%B3%95%E5%B7%A5%E7%A8%8B%E5%B8%88',
        'sec-ch-ua': '"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        '_': '1695108469569',#不知道干嘛的 反正每次网站搜索要变
    }

    data = {
        'requestFrom': '1',
        'page': '26',#页数
        'pageSize': '20',
        'recruitType': '3',
        'pageSource': '5001',
        'query': f'{key}',#关键词
        'visitorId': '1fa5bb6c-c77e-4b7c-9122-51e609c614d7',
    }

    response = requests.post('https://www.nowcoder.com/np-api/u/job/search', params=params, cookies=cookies, headers=headers, data=data)

    print(response.text)



    cookies = {
        'NOWCODERUID': '186A76E083F10CADEEFE2B95950E7B24',
        'NOWCODERCLINETID': '66EC9833B0A846AD902AE0887564D796',
        'gr_user_id': '1fa5bb6c-c77e-4b7c-9122-51e609c614d7',
        '_bl_uid': '2wl4th8mchXyjgrOhutXupb6Uh5w',
        'c196c3667d214851b11233f5c17f99d5_gr_last_sent_cs1': '261863240',
        'YD00000586307807%3AWM_TID': 'elQRobNlZhlBVUUUQFaAKqogiGhtmj9E',
        'YD00000586307807%3AWM_NI': 'vBoX3ciBWTDhKLifhEAxG%2FO0sbOjpd9bVI3528M%2FPSD4PUwTt5idqtYASO0mJJ%2FrBnE92He183N8JYgUuwuwb6BIrNXpN31sj04WpMmP5ZwL725bHzm3hxhqnfAE33sBZVc%3D',
        'YD00000586307807%3AWM_NIKE': '9ca17ae2e6ffcda170e2e6eebbe45b958bbc85ef3a85eb8ea2d55a879f8e86c874928abed3cf6eb0b5e1d8d92af0fea7c3b92ab69ea1b9b269ab9e99b5c7648994a787eb4f83a889d0ce3cb1be818bf370fbbe9aaab23ff2e883d0d35988eca0b6f660b8eba785f4809b9f9db0b3678a96e193c16687e7fea9e83bfced82d9c953a58bbb98f87da2ea8eaaf1469cb082d4b479aaf0fcb8f347af90fbbbf648f5eefb83cb72afeda899eb7baeba8fa6b239b19e96b7e237e2a3',
        'c196c3667d214851b11233f5c17f99d5_gr_session_id': '36043343-941c-49b1-ac67-509c9e7be7cf',
        'c196c3667d214851b11233f5c17f99d5_gr_session_id_36043343-941c-49b1-ac67-509c9e7be7cf': 'true',
        'acw_tc': '6a95a8c22643e0d321f11bd993ce4fdd0bea46254256c4e627dbf1ca72bce74e',
        'csrfToken': 'jqGFRyOtFj89iGJiL70k1v9f',
        'Hm_lvt_a808a1326b6c06c437de769d1b85b870': '1692880486,1695103766,1695107008,1695109969',
        'SERVERID': '4500890894435736ae70a9add3498842|1695110119|1695109974',
        'SERVERCORSID': '4500890894435736ae70a9add3498842|1695110119|1695109974',
        'Hm_lpvt_a808a1326b6c06c437de769d1b85b870': '1695110112',
    }

    headers = {
        'authority': 'www.nowcoder.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'NOWCODERUID=186A76E083F10CADEEFE2B95950E7B24; NOWCODERCLINETID=66EC9833B0A846AD902AE0887564D796; gr_user_id=1fa5bb6c-c77e-4b7c-9122-51e609c614d7; _bl_uid=2wl4th8mchXyjgrOhutXupb6Uh5w; c196c3667d214851b11233f5c17f99d5_gr_last_sent_cs1=261863240; YD00000586307807%3AWM_TID=elQRobNlZhlBVUUUQFaAKqogiGhtmj9E; YD00000586307807%3AWM_NI=vBoX3ciBWTDhKLifhEAxG%2FO0sbOjpd9bVI3528M%2FPSD4PUwTt5idqtYASO0mJJ%2FrBnE92He183N8JYgUuwuwb6BIrNXpN31sj04WpMmP5ZwL725bHzm3hxhqnfAE33sBZVc%3D; YD00000586307807%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eebbe45b958bbc85ef3a85eb8ea2d55a879f8e86c874928abed3cf6eb0b5e1d8d92af0fea7c3b92ab69ea1b9b269ab9e99b5c7648994a787eb4f83a889d0ce3cb1be818bf370fbbe9aaab23ff2e883d0d35988eca0b6f660b8eba785f4809b9f9db0b3678a96e193c16687e7fea9e83bfced82d9c953a58bbb98f87da2ea8eaaf1469cb082d4b479aaf0fcb8f347af90fbbbf648f5eefb83cb72afeda899eb7baeba8fa6b239b19e96b7e237e2a3; c196c3667d214851b11233f5c17f99d5_gr_session_id=36043343-941c-49b1-ac67-509c9e7be7cf; c196c3667d214851b11233f5c17f99d5_gr_session_id_36043343-941c-49b1-ac67-509c9e7be7cf=true; acw_tc=6a95a8c22643e0d321f11bd993ce4fdd0bea46254256c4e627dbf1ca72bce74e; csrfToken=jqGFRyOtFj89iGJiL70k1v9f; Hm_lvt_a808a1326b6c06c437de769d1b85b870=1692880486,1695103766,1695107008,1695109969; SERVERID=4500890894435736ae70a9add3498842|1695110119|1695109974; SERVERCORSID=4500890894435736ae70a9add3498842|1695110119|1695109974; Hm_lpvt_a808a1326b6c06c437de769d1b85b870=1695110112',
        'origin': 'https://www.nowcoder.com',
        'pragma': 'no-cache',
        'referer': 'https://www.nowcoder.com/jobs/fulltime/center?recruitType=3&search=%E7%AE%97%E6%B3%95%E5%B7%A5%E7%A8%8B%E5%B8%88',
        'sec-ch-ua': '"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        '_': '1695110158118',
    }

    data = {
        'careerJobId': '',
        'jobCity': '',
        'page': '26',
        'query': '算法工程师',
        'random': 'true',
        'recommend': 'false',
        'recruitType': '1',
        'salaryType': '2',
        'pageSize': '20',
        'requestFrom': '1',
        'order': '0',
        'pageSource': '5001',
        'visitorId': '1fa5bb6c-c77e-4b7c-9122-51e609c614d7',
    }

    response = requests.post('https://www.nowcoder.com/np-api/u/job/search', params=params, cookies=cookies, headers=headers, data=data)
    print(response.text)
    data=json.loads(response.text)
    totol_page=data['data']['totalPage']
    currentpage=data['data']['currentPage']
    if(currentpage>totol_page):
        print('爆页了')
    if(data['code']!=0):
        print('IP G了')   
    print()
    with open('牛客校招.txt', 'w', encoding='utf-8-sig') as f:
    f.write(response.text)
    rows=[]
    for data in data["data"]['datas']:
        info=dict()
        info['jobName']=data['jobName']
        print()
        infos=json.loads(data['ext'])
        infos = infos.get('infos', '')
        requirements = data.get('requirements', '')
        info['capability']=requirements
        info['jobCityList']=data['jobCityList']
        info['graduationYear']=data['graduationYear']
        info['jobKeys']=data['jobKeys']
        info['salarymin']=data['salaryMin']
        info['salarymax']=data['salaryMax']
        print(data['user'])
        info['companyName']=data['user']['identity'][0]['companyName']
        rows.append(info)
    # 将数据写入CSV文件
    with open('牛客校招.csv', 'a', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)



def social(key='算法工程师'):
    cookies = {
        'NOWCODERUID': '186A76E083F10CADEEFE2B95950E7B24',
        'NOWCODERCLINETID': '66EC9833B0A846AD902AE0887564D796',
        'gr_user_id': '1fa5bb6c-c77e-4b7c-9122-51e609c614d7',
        '_bl_uid': '2wl4th8mchXyjgrOhutXupb6Uh5w',
        'c196c3667d214851b11233f5c17f99d5_gr_last_sent_cs1': '261863240',
        'YD00000586307807%3AWM_TID': 'elQRobNlZhlBVUUUQFaAKqogiGhtmj9E',
        'YD00000586307807%3AWM_NI': 'vBoX3ciBWTDhKLifhEAxG%2FO0sbOjpd9bVI3528M%2FPSD4PUwTt5idqtYASO0mJJ%2FrBnE92He183N8JYgUuwuwb6BIrNXpN31sj04WpMmP5ZwL725bHzm3hxhqnfAE33sBZVc%3D',
        'YD00000586307807%3AWM_NIKE': '9ca17ae2e6ffcda170e2e6eebbe45b958bbc85ef3a85eb8ea2d55a879f8e86c874928abed3cf6eb0b5e1d8d92af0fea7c3b92ab69ea1b9b269ab9e99b5c7648994a787eb4f83a889d0ce3cb1be818bf370fbbe9aaab23ff2e883d0d35988eca0b6f660b8eba785f4809b9f9db0b3678a96e193c16687e7fea9e83bfced82d9c953a58bbb98f87da2ea8eaaf1469cb082d4b479aaf0fcb8f347af90fbbbf648f5eefb83cb72afeda899eb7baeba8fa6b239b19e96b7e237e2a3',
        'acw_tc': 'bdf0fb3869e27413df60dfb0a3013eeb4f37171723271caf1de3c0cce5b0de7b',
        'csrfToken': '_RzhvYbLjpvtdOx7hIN_o2gO',
        'Hm_lvt_a808a1326b6c06c437de769d1b85b870': '1692880486,1695103766,1695107008',
        'c196c3667d214851b11233f5c17f99d5_gr_session_id': '36043343-941c-49b1-ac67-509c9e7be7cf',
        'c196c3667d214851b11233f5c17f99d5_gr_session_id_36043343-941c-49b1-ac67-509c9e7be7cf': 'true',
        'SERVERID': '4500890894435736ae70a9add3498842|1695108468|1695107014',
        'SERVERCORSID': '4500890894435736ae70a9add3498842|1695108468|1695107014',
        'Hm_lpvt_a808a1326b6c06c437de769d1b85b870': '1695108461',
    }

    headers = {
        'authority': 'www.nowcoder.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'NOWCODERUID=186A76E083F10CADEEFE2B95950E7B24; NOWCODERCLINETID=66EC9833B0A846AD902AE0887564D796; gr_user_id=1fa5bb6c-c77e-4b7c-9122-51e609c614d7; _bl_uid=2wl4th8mchXyjgrOhutXupb6Uh5w; c196c3667d214851b11233f5c17f99d5_gr_last_sent_cs1=261863240; YD00000586307807%3AWM_TID=elQRobNlZhlBVUUUQFaAKqogiGhtmj9E; YD00000586307807%3AWM_NI=vBoX3ciBWTDhKLifhEAxG%2FO0sbOjpd9bVI3528M%2FPSD4PUwTt5idqtYASO0mJJ%2FrBnE92He183N8JYgUuwuwb6BIrNXpN31sj04WpMmP5ZwL725bHzm3hxhqnfAE33sBZVc%3D; YD00000586307807%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eebbe45b958bbc85ef3a85eb8ea2d55a879f8e86c874928abed3cf6eb0b5e1d8d92af0fea7c3b92ab69ea1b9b269ab9e99b5c7648994a787eb4f83a889d0ce3cb1be818bf370fbbe9aaab23ff2e883d0d35988eca0b6f660b8eba785f4809b9f9db0b3678a96e193c16687e7fea9e83bfced82d9c953a58bbb98f87da2ea8eaaf1469cb082d4b479aaf0fcb8f347af90fbbbf648f5eefb83cb72afeda899eb7baeba8fa6b239b19e96b7e237e2a3; acw_tc=bdf0fb3869e27413df60dfb0a3013eeb4f37171723271caf1de3c0cce5b0de7b; csrfToken=_RzhvYbLjpvtdOx7hIN_o2gO; Hm_lvt_a808a1326b6c06c437de769d1b85b870=1692880486,1695103766,1695107008; c196c3667d214851b11233f5c17f99d5_gr_session_id=36043343-941c-49b1-ac67-509c9e7be7cf; c196c3667d214851b11233f5c17f99d5_gr_session_id_36043343-941c-49b1-ac67-509c9e7be7cf=true; SERVERID=4500890894435736ae70a9add3498842|1695108468|1695107014; SERVERCORSID=4500890894435736ae70a9add3498842|1695108468|1695107014; Hm_lpvt_a808a1326b6c06c437de769d1b85b870=1695108461',
        'origin': 'https://www.nowcoder.com',
        'pragma': 'no-cache',
        'referer': 'https://www.nowcoder.com/jobs/fulltime/center?recruitType=3&search=%E7%AE%97%E6%B3%95%E5%B7%A5%E7%A8%8B%E5%B8%88',
        'sec-ch-ua': '"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        '_': '1695108469569',#不知道干嘛的 反正每次网站搜索要变
    }

    data = {
        'requestFrom': '1',
        'page': '26',#页数
        'pageSize': '20',
        'recruitType': '3',
        'pageSource': '5001',
        'query': f'{key}',#关键词
        'visitorId': '1fa5bb6c-c77e-4b7c-9122-51e609c614d7',
    }

    response = requests.post('https://www.nowcoder.com/np-api/u/job/search', params=params, cookies=cookies, headers=headers, data=data)
    data=json.loads(response.text)
    totol_page=data['data']['totalPage']
    currentpage=data['data']['currentPage']
    if(currentpage>totol_page):
        print('爆页了')
    if(data['code']!=0):
        print('IP G了')   
    print()
    with open('牛客校招.txt', 'w', encoding='utf-8-sig') as f:
            f.write(response.text)
    rows=[]
    for data in data["data"]['datas']:
        info=dict()
        info['jobName']=data['jobName']
        print()
        infos=json.loads(data['ext'])
        infos = infos.get('infos', '')
        requirements = data.get('requirements', '')
        info['capability']=requirements
        info['jobCityList']=data['jobCityList']
        info['graduationYear']=data['graduationYear']
        info['jobKeys']=data['jobKeys']
        info['salarymin']=data['salaryMin']
        info['salarymax']=data['salaryMax']
        print(data['user'])
        info['companyName']=data['user']['identity'][0]['companyName']
        rows.append(info)
    # 将数据写入CSV文件
    with open('牛客社招.csv', 'a', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
