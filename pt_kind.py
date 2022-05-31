from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time
import requests
import csv
import time
from lxml import etree

headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
'Cookie':'cgbt_password=4a5e91ad19ee59c0bf1903ca0dd8ff589cf36624/REGTuJ/PNMO7IPsyWjNVkwSfFH5OpJVtBcuJ9EWeIzph5/FyCFdgdhz7lpji0eFpFxz8zAoBWFBHR6D; cgbt_uid=61db99eb17a44e2e4332ef220b4ea5f7698bb51faiw5Rt1WmBhfmZvKc//WpyPmwLwYY2mk; zhixing_9328_saltkey=FoCczRWj; zhixing_9328_lastvisit=1653205886; zhixing_9328_sid=SW2K25; zhixing_9328_sendmail=1; zhixing_9328_ulastactivity=e85fBACLElMnw9zWLj+LBHKxI+Yd1Gnme0eflmivU1FeFy0dNOZ+; zhixing_9328_auth=ddc8yt3L4kwPJ9qc4ai7w+AQQ16oezTmUjjO7pjBy56SOqwjSkaPVH8msU/xtA3FaxXpun9K8Htes3vQ7auEUtwLQ48; zhixing_9328_lastcheckfeed=390353|1653209515; zhixing_9328_checkfollow=1; zhixing_9328_lip=219.242.247.173,1653206844; zhixing_9328_lastact=1653209516	home.php	spacecp; zhixing_9328_checkpm=1'
}

kind_list=['movie','music','game','sports','study']
for kind in kind_list:
    fp = open('./%s.csv'%kind,'w',newline = '',encoding='utf-8')
    fp_write=csv.writer(fp)
    fp_write.writerow(['序号','名称','网址后缀'])
    for i in range(10):
        s_url="http://pt.zhixing.bjtu.edu.cn/search/%s/p%d"%(kind,i+1)
        res = requests.get(s_url,headers=headers) #发起请求
        res.encoding='utf-8' #设置编码格式
        text = res.text
        print(text)
        html = etree.HTML(text)
        for j in range(20):
            ID=i*20+j+1
            title = html.xpath("//*[@class='torrenttable']/tr[%d]/td[2]/a/text()"%(j+2))
            http = html.xpath('//*[@class="torrenttable"]/tr[%d]/td[2]/a/@href'%(j+2))

            fp_write.writerow(['%d'%ID,'%s'%title,'%s'%http])
