from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import exceptions

import time
options = ChromeOptions()
#控制无头浏览器
#options.add_argument('--headless')
# 以最高权限运行
options.add_argument('--no-sandbox')
# navigator.webdriver 设置为 false
options.add_argument("--disable-blink-features=AutomationControlled")

# 隐藏"Chrome正在受到自动软件的控制"提示
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
#设置浏览器exe位置
driver = webdriver.Chrome(options=options)
with open("D:\codeprogram\Web_Crawling_Engineer\Seleniun配置\stealth.min.js", 'r') as f:
    js = f.read()
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': js})
key="python"
driver.get('https://www.liepin.com/')
i=input()
Input = driver.find_elements(By.XPATH, '//*[@id="home-search-bar-container"]/div/div/div/div/div/div[1]/div[1]/div/div/div/input')
Input.send_keys(f"{key}")   
jobs = driver.find_element(By.XPATH,'//*[@id="lp-search-job-box"]/div[3]/section[1]/div[1]') 
next_button=None
print(page)
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
            reward=job_info.find_element(By.CLASS_NAME,'job-list-item-bottom').text

        except exceptions.NoSuchElementException:
            reward="无"

        print("职位名称:", job_name)
        print("薪资:", money)
        print("地区、时间和学历要求:", area_time_academic)
        print("公司名称:", company)
        print('福利',reward)
        print("------------------------")
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