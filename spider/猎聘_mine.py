from playwright.sync_api import Playwright, sync_playwright, expect
import json
import csv
import os
import random
def scroll_down_page(page):
    # 获取页面高度
    page_height = page.evaluate('''() => {
        return Math.max(
            document.documentElement.clientHeight,
            window.innerHeight || 0
        );
    }''')

    # 模拟滚动到页面底部
    page.evaluate(f'''(pageHeight) => {{
        window.scrollTo({{top: pageHeight, behavior: 'smooth'}});
    }}''', page_height)

def save_href(key,hrefs,model='a+'):
    """
    传入hrefs 字符串
    """
    with open(f'{key}_href.txt',model,encoding='utf-8') as f:
            f.write(hrefs)

def all_pagesurl_save(page,key):
    filename=f'{key}_href.txt'
    if os.path.exists(filename):
        return []
    page.goto("https://www.liepin.com/")
    page.get_by_placeholder("搜索职位/公司/内容关键词").click()
    page.get_by_placeholder("搜索职位/公司/内容关键词").fill(f"{key}")
    page.get_by_placeholder("搜索职位/公司/内容关键词").press("Enter")
    #获取详情页url
    pagenum=page.locator('xpath=//*[@id="lp-search-job-box"]/div[3]/section[1]/div[2]/ul//a').last.text_content()
    print(pagenum)
    hrefs=''
    with open(filename,'w+',encoding='utf-8') as f:
        for html in range(int(pagenum)):
            page.wait_for_timeout(1000)
            urls=page.locator("xpath=//*[@class='job-list-box']//a").all()
            #print(urls)
            for url in urls:
                href = url.get_attribute('href')
                hrefs+=(href+'\n')    
            scroll_down_page(page)
            if page.get_by_role("button", name="right").is_disabled():
                print('爬取页面完成')
                break
            page.get_by_role("button", name="right").click()
            # ---------------------
            f.write(hrefs)
    return hrefs
def all_url_get_file(key):
    filename=f"{key}_href.txt"
    urls = []
    with open(filename, 'r') as file:
        for line in file:
            url = line.strip()  # 去除行末尾的换行符和空格
            urls.append(url)
    return urls
def all_pagesurl_get(page,key):
    page.goto("https://www.liepin.com/")
    page.wait_for_timeout(random.randint(1000,3000))

    page.get_by_placeholder("搜索职位/公司/内容关键词").click()
    page.get_by_placeholder("搜索职位/公司/内容关键词").fill(f"{key}")
    page.get_by_placeholder("搜索职位/公司/内容关键词").press("Enter")
    #获取详情页url
    pagenum=page.locator('xpath=//*[@id="lp-search-job-box"]/div[3]/section[1]/div[2]/ul//a').last.text_content()
    hrefs=[]
    for html in range(int(pagenum)):
        page.wait_for_timeout(1000)
        urls=page.locator("xpath=//*[@class='job-list-box']//a").all()
        #print(urls)
        #获得详情页的href
        for url in urls:
            href = url.get_attribute('href')
            hrefs.append(href)    
        scroll_down_page(page)
        if page.get_by_role("button", name="right").is_disabled():
            print('爬取页面完成')
            break
        page.get_by_role("button", name="right").click()
        # ---------------------
    return hrefs
def test(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    key='python'
    page.goto("https://www.liepin.com/")
    page.get_by_placeholder("搜索职位/公司/内容关键词").click()
    page.get_by_placeholder("搜索职位/公司/内容关键词").fill("python")
    page.get_by_placeholder("搜索职位/公司/内容关键词").press("Enter")
    #获取详情页url
    pagenum=page.locator('xpath=//*[@id="lp-search-job-box"]/div[3]/section[1]/div[2]/ul//a').last.text_content()
    print(pagenum)
    with open(f'{key}href.txt','a+',encoding='utf-8') as f:
        for html in range(int(pagenum)):
            page.wait_for_timeout(1000)
            urls=page.locator("xpath=//*[@class='job-list-box']//a").all()
            print(urls)
            hrefs=""#获得详情页的href
            for url in urls:
                href = url.get_attribute('href')
                hrefs+=(href+'\n')    
            scroll_down_page(page)
            if page.get_by_role("button", name="right").is_disabled():
                print('爬取页面完成')
                break
            page.get_by_role("button", name="right").click()
            # ---------------------
            f.write(hrefs)
    context.close()
    browser.close()

def save_details(page,urls,key):
    "传入urls 进行爬取"
    filename = f'{key}_liepindata.csv'
    with open(filename, 'a+', newline='',encoding='utf-8') as csvfile:
      for url in urls:
        scroll_down_page(page)
        page.goto(url)
        page.wait_for_timeout(random.randint(1000,3000))
        try:
            position = page.locator('xpath=//*[@class="name ellipsis-1"]').first.text_content()
        except Exception as e:
            position = None

        try:
            salary = page.locator('xpath=//*[@class="salary"]').first.text_content()
        except Exception as e:
            salary = None

        try:
            data = page.locator('xpath=//*[@class="job-properties"]/span').all_text_contents()
            data = [item for item in data if item != '']
        except Exception as e:
            data = []

        try:
            goods = page.locator('xpath=//*[@class="labels"]').first.text_content().split()
        except Exception as e:
            goods = []

        try:
            capacity = page.locator('xpath=//*[@class="tag-box"]').text_content().split()
        except Exception as e:
            capacity = []

        try:
            job_detail = page.locator('xpath=//dd[@data-selector="job-intro-content"]').text_content()
        except Exception as e:
            job_detail = None
        print(position,salary,data,job_detail,capacity)#local,time,academic)
        print(goods)
        data = {
        '职位': position,
        '工资': salary,
        '工作地区、工作年限、学历': data,
        '工作需要': capacity,
        '福利': goods,
        '工作详细': job_detail,

        } 


        # 将字典的键作为CSV文件的列名
        fieldnames = data.keys()

        # 将字典的值作为CSV文件的行数据
        rows = [data]

        # 写入CSV文件
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if  csvfile.tell() == 0:
            writer.writeheader()
        writer.writerows(rows)
def save_line(line,key):
    with open(f"{key}_ing.txt", "w", encoding="utf-8") as f:
             f.write(str(line))
def save_details_from_file(page,key):
    "传入urls 进行爬取"
    href_txt=f'{key}_href.txt'
    filename = f'{key}_liepindata.csv'
    ingfile=f"{key}_ing.txt"
    line_number =0
    try:
        with open(href_txt, 'r') as rows:
            if (os.path.exists(ingfile)):
                with open(ingfile, 'r') as f:
                    line_number =int(f.read())
            with open(filename, 'a+', newline='',encoding='utf-8') as csvfile:
                for i,line in enumerate(rows, start=line_number):
                    line_number += 1
                    href = line.strip()
                    #print(href)
                    page.goto(href)
                    scroll_down_page(page)
                    page.wait_for_timeout(random.randint(1000,3000))
                    try:
                        campany_name = page.locator('xpath=/html/body/main/aside/div[2]/div[1]/div[1]').text_content().strip()
                        print(campany_name)
                    except Exception as e:
                        print('1',e)
                        campany_name = ''
                    try:
                        campany_info = page.locator('xpath=//*[@class="company-other"]//span[@class="text"]').all_text_contents()
                        print(campany_info)
                    except Exception as e:
                        print('1',e)
                        campany_info = ''
                    try:
                        position = page.locator('xpath=//*[@class="name ellipsis-1"]').first.text_content()
                    except Exception as e:
                        print('1',e)
                        position = None

                    try:
                        salary = page.locator('xpath=//*[@class="salary"]').first.text_content()
                    except Exception as e:
                        print('2',e)
                        salary = None
                    try:
                        salary = page.locator('xpath=//*[@class="salary"]').first.text_content()
                    except Exception as e:
                        print('2',e)
                        salary = None

                    try:
                        data = page.locator('xpath=//*[@class="job-properties"]/span').all_text_contents()
                        data = [item for item in data if item != '']
                    except Exception as e:
                        print('3',e)

                        data = []

                    try:
                        goods = page.locator('xpath=//*[@class="labels"]').first.text_content().split()
                    except Exception as e:
                        print('4',e)
                        goods = []

                    try:
                        capacity = page.locator('xpath=//*[@class="tag-box"]').text_content().split()
                    except Exception as e:
                        print('5',e)

                        capacity = []

                    try:
                        job_detail = page.locator('xpath=//dd[@data-selector="job-intro-content"]').text_content()
                    except Exception as e:
                        print('6',e)
                        job_detail = None

                    #print(position,salary,data,job_detail,capacity)#local,time,academic)
                    #print(goods)
                    data = {
                    '职位': position,
                    '工资': salary,
                    '工作地区、工作年限、学历': data,
                    '工作需要': capacity,
                    '福利': goods,
                    '工作详细': job_detail,
                    '公司名称':campany_name,
                    '公司信息':campany_info,
                    '详情页': href
                    } 


                    # 将字典的键作为CSV文件的列名
                    fieldnames = data.keys()

                    # 将字典的值作为CSV文件的行数据
                    rows = [data]

                    # 写入CSV文件
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    if csvfile.tell() == 0:
                        writer.writeheader()
                    writer.writerows(rows)
                    print("成功")
    except Exception as e:
        print(e)
    finally:
      try:
        save_line(line_number)
      except Exception as e:
          print('保存进程失败')

def save_one_details(page,url):
    "传入urls 进行爬取"
    with open(filename, 'a+', newline='',encoding='utf-8') as csvfile:
        page.goto(url)
        position=page.locator('xpath=//*[@class="name ellipsis-1"]').first.text_content()
        salary=page.locator('xpath=//*[@class="salary"]').first.text_content()
        #local,time,academic tag-box
        data =page.locator('xpath=//*[@class="job-properties"]/span').all_text_contents()
        data = [item for item in data if item != '']
        goods=page.locator('xpath=//*[@class="labels"]').first.text_content().split()
        capacity=page.locator('xpath=//*[@class="tag-box"]').text_content().split()
        job_detail=page.locator('xpath=//dd[@data-selector="job-intro-content"]').text_content()
        local,time,academic=data
        print(position,salary,local,time,academic,job_detail,capacity)#local,time,academic)
        print(goods)
        data = {
        '职位': position,
        '工资': salary,
        '工作地区': local,
        '工作年限': time,
        '学历': academic,
        '工作需要': capacity,
        '福利': goods,
        '工作详细': job_detail,
        '详情页':url
        } 

        filename = 'liepindata.csv'

        # 将字典的键作为CSV文件的列名
        fieldnames = data.keys()

        # 将字典的值作为CSV文件的行数据
        rows = [data]

        # 写入CSV文件
        reader = csv.reader(csvfile)
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        has_content = any(row for row in reader)
        if not has_content:
            writer.writeheader()
        writer.writerows(rows)
    print("数据已成功保存到 liepindata.csv 文件中")
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    key="C语言"
    urls=all_pagesurl_save(page,key)
    save_details_from_file(page,key)
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
