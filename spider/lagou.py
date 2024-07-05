import requests

cookies = {
    'RECOMMEND_TIP': 'true',
    'user_trace_token': '20230919092945-3178a9f0-4438-4073-a33d-83f0d834f5fa',
    'LGUID': '20230919092945-519b104b-678a-407f-9f88-61bb7a9539bf',
    '_ga': 'GA1.2.262811108.1695086977',
    'X_HTTP_TOKEN': '2b4e06f68129ba6954053379618dd973a66c0c6d7d',
    'JSESSIONID': 'ABAAABAABAGABFA50AFB7FFC7FA56BB2A9D8AE375115724',
    'WEBTJ-ID': '20231022075535-18b54aa66178ab-0e0a41d8b265fc-745d5771-1327104-18b54aa661818a8',
    'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1697334539,1697334622,1697334871,1697932536',
    'sensorsdata2015session': '%7B%7D',
    '_gid': 'GA1.2.1810776591.1697932536',
    '_gat': '1',
    'privacyPolicyPopup': 'false',
    'PRE_UTM': '',
    'PRE_LAND': 'https%3A%2F%2Fwww.lagou.com%2F',
    'LGSID': '20231022075538-4c3f3aed-8a2c-4b4e-b630-b9ebcb3d1972',
    'PRE_HOST': 'cn.bing.com',
    'PRE_SITE': 'https%3A%2F%2Fcn.bing.com%2F',
    'index_location_city': '%E5%85%A8%E5%9B%BD',
    'TG-TRACK-CODE': 'index_search',
    '__lg_stoken__': '521d3c96ad259b4ac1dd43efe16522f8d9d08b74def69fb8b8f625d617d59bf33d1b0999fa8755b7a721692766155d6f01fe65e3a13d387efd921eb320c802270d9265f38b33',
    'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1697932552',
    'LGRID': '20231022075553-60284744-2cbb-4a2d-bbe9-d9f5f7e0d220',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2218aab0e9fb0bb0-0993e13f834f7c-78505774-1327104-18aab0e9fb11022%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcn.bing.com%2F%22%2C%22%24latest_utm_source%22%3A%22pc_search_right_jljx_1%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%22118.0.0.0%22%7D%2C%22%24device_id%22%3A%2218aab0e9fb0bb0-0993e13f834f7c-78505774-1327104-18aab0e9fb11022%22%7D',
    '_ga_DDLTLJDLHH': 'GS1.2.1697932537.12.1.1697932552.45.0.0',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'RECOMMEND_TIP=true; user_trace_token=20230919092945-3178a9f0-4438-4073-a33d-83f0d834f5fa; LGUID=20230919092945-519b104b-678a-407f-9f88-61bb7a9539bf; _ga=GA1.2.262811108.1695086977; X_HTTP_TOKEN=2b4e06f68129ba6954053379618dd973a66c0c6d7d; JSESSIONID=ABAAABAABAGABFA50AFB7FFC7FA56BB2A9D8AE375115724; WEBTJ-ID=20231022075535-18b54aa66178ab-0e0a41d8b265fc-745d5771-1327104-18b54aa661818a8; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1697334539,1697334622,1697334871,1697932536; sensorsdata2015session=%7B%7D; _gid=GA1.2.1810776591.1697932536; _gat=1; privacyPolicyPopup=false; PRE_UTM=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGSID=20231022075538-4c3f3aed-8a2c-4b4e-b630-b9ebcb3d1972; PRE_HOST=cn.bing.com; PRE_SITE=https%3A%2F%2Fcn.bing.com%2F; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_search; __lg_stoken__=521d3c96ad259b4ac1dd43efe16522f8d9d08b74def69fb8b8f625d617d59bf33d1b0999fa8755b7a721692766155d6f01fe65e3a13d387efd921eb320c802270d9265f38b33; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1697932552; LGRID=20231022075553-60284744-2cbb-4a2d-bbe9-d9f5f7e0d220; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218aab0e9fb0bb0-0993e13f834f7c-78505774-1327104-18aab0e9fb11022%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcn.bing.com%2F%22%2C%22%24latest_utm_source%22%3A%22pc_search_right_jljx_1%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%22118.0.0.0%22%7D%2C%22%24device_id%22%3A%2218aab0e9fb0bb0-0993e13f834f7c-78505774-1327104-18aab0e9fb11022%22%7D; _ga_DDLTLJDLHH=GS1.2.1697932537.12.1.1697932552.45.0.0',
    'Pragma': 'no-cache',
    'Referer': 'https://www.lagou.com/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61',
    'sec-ch-ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'labelWords': '',
    'fromSearch': 'true',
    'suginput': '',
    'kd': 'web',
}

response = requests.get('https://www.lagou.com/wn/jobs', params=params, cookies=cookies, headers=headers)
if response.status_code == 200:
    # 保存响应内容到文件
    with open('page.txt', 'w+', encoding='utf-8') as f:
        print(response.text)
        f.write(response.text)
        print("页面保存成功！")
else:
    print("请求失败，无法保存页面。")