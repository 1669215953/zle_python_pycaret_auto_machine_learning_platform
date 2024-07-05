from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import exceptions
import csv
import time
fieldnames = ['职位名称', '薪资', '地区、时间和学历要求', '公司名称', '福利']

options = ChromeOptions()
#控制无头浏览器
#options.add_argument('--headless')
# 以最高权限运行
options.add_argument('--no-sandbox')
# navigator.webdriver 设置为 false
options.add_argument("--disable-blink-features=AutomationControlled")
# 指定要保存的 CSV 文件路径
csv_file = f'前程无忧.csv'

# 使用 'w' 模式打开文件，并创建 CSV 写入器



# 隐藏"Chrome正在受到自动软件的控制"提示
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
#设置浏览器exe位置

keys=input().split(' ')
for key in keys:
    driver = webdriver.Chrome(options=options)
    with open("D:\codeprogram\Web_Crawling_Engineer\Seleniun配置\stealth.min.js", 'r') as f:
       js = f.read()
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': js})
    try:
        driver.get(f'https://we.51job.com/pc/search?keyword={key}&searchType=2&sortType=0&metro=')
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div')
                )
            )
        except exceptions.TimeoutException:
            print("超时")
        job_list_elements = driver.find_elements(By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div')
        page = driver.find_element(By.XPATH,"//ul[@class='el-pager']/li[last()]").text
        next_button=None
        print(page)

        with open(csv_file, 'w', newline='', encoding='utf-8') as file:
            for i in range(int(page)):
                try:
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_all_elements_located(
                            (By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div')
                        )
                    )
                except exceptions.TimeoutException:
                    print("超时")
                job_list_elements = driver.find_elements(By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div')
                driver.execute_script('document.documentElement.scrollTop = document.documentElement.scrollHeight')
                for job_info in job_list_elements:
                    # 输出节点的文本信息
                    try:
                        WebDriverWait(driver, 10).until(
                            EC.presence_of_all_elements_located(
                                (By.CLASS_NAME,'jname.text-cut')
                            )
                        )
                    except exceptions.TimeoutException:
                        print('元素加载超时')
                    job_name=job_info.find_element(By.CLASS_NAME,'jname.text-cut').text
                    money=job_info.find_element(By.CLASS_NAME,'sal.shrink-0').text
                    area_time_academic=job_info.find_element(By.CLASS_NAME,'d.text-cut').text
                    company=job_info.find_element(By.CLASS_NAME,'cname.text-cut').text
                    try:  # 有的公司没有公司介绍
                        reward=job_info.find_element(By.CLASS_NAME,'job-list-item-bottom').text.split('\n')

                    except exceptions.NoSuchElementException:
                        reward=""
                    data = [
                        {
                            '职位名称': job_name,
                            '薪资': money,
                            '地区、时间和学历要求': area_time_academic,
                            '公司名称': company,
                            '福利': reward
                        }
                        # 假设您有多个职位信息，可以在此处添加更多字典
                    ]
                    print("职位名称:", job_name)
                    print("薪资:", money)
                    print("地区、时间和学历要求:", area_time_academic)
                    print("公司名称:", company)
                    print('福利',reward)
                    print("------------------------")
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    # 写入字段名
                    writer.writeheader()

                    # 写入数据
                    writer.writerows(data)
                try:
                            WebDriverWait(driver, 10).until(
                                EC.presence_of_all_elements_located(
                                    (By.CLASS_NAME,'btn-next')
                                )
                            )
                except exceptions.TimeoutException:
                    print('元素加载超时')
                next_button=driver.find_element(By.CLASS_NAME,'btn-next').click()




        driver.quit()
    except exceptions.TimeoutException:
            print("超时")