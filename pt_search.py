from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time
import csv
import time
from lxml import etree

#第一次需要获取cookies来实现后续的免密登录
driver = webdriver.Chrome()
driver.get("http://pt.zhixing.bjtu.edu.cn/search/")

for i in range(0, 30):
    print(30 - i)
    time.sleep(1)

# 获取cookies
cookies = driver.get_cookies()

# 保存到本地
f1 = open('cookie.txt', 'w')  # cookies存入文件JSON字符串
f1.write(json.dumps(cookies))
f1.close()

driver.close()

kind_list=['movie','study','sports','game','music']
for kind in kind_list:
    for i in range(200):
        fp = open('./%s_%d.csv'%(kind,i+1),'w',newline = '',encoding='utf-8')
        fp_write=csv.writer(fp)
        fp_write.writerow(['用户名','用户组','用户ID','完成时间'])

        if i>=1:
            driver.close()#关闭上一次循环打开的网页
        driver = webdriver.Chrome()
        driver.get("http://pt.zhixing.bjtu.edu.cn/search/")
        f1 = open('cookie.txt')
        cookie = f1.read()
        cookie_list = json.loads(cookie)  # json读取cookies
        for c in cookie_list:
            driver.add_cookie(c)
        driver.refresh()
        with open('%s.csv'%kind,encoding='utf-8') as ccc:
            reader=csv.reader(ccc)
            for index,lines in enumerate(reader):
                if index==i+1:
                    row=lines
        http_tail=row[2][2:-2]
        driver.get('http://pt.zhixing.bjtu.edu.cn'+http_tail)
        time.sleep(1)
        try:
            driver.find_element(by=By.XPATH, value="//*[@id='ct']/div[1]/div[3]/div[4]/span[5]").click()
        except:
            time.sleep(1800)
            i=i-1
            continue


        #print(driver.page_source)
        time.sleep(1)
        for j in range(500):
            try:
                user_name = driver.find_element(by=By.XPATH,value="//*[@id='torrent-detail-done']/table/tbody/tr[%d]/td[1]/a"%(j+2)).text
                user_level = driver.find_element(by=By.XPATH,value="//*[@id='torrent-detail-done']/table/tbody/tr[%d]/td[2]"%(j+2)).text
                user_ID = driver.find_element(by=By.XPATH, value="//*[@id='torrent-detail-done']/table/tbody/tr[%d]/td[3]"%(j+2)).text
                download_time = driver.find_element(by=By.XPATH,value="//*[@id='torrent-detail-done']/table/tbody/tr[%d]/td[4]"%(j+2)).text
                fp_write.writerow(['%s'%user_name,'%s'%user_level,'%s'%user_ID,'%s'%download_time])
                time.sleep(0.01)
            except:
                break

#print(driver.page_source)