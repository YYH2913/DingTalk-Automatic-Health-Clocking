#-*-coding:utf-8 -*-
from selenium import webdriver
import datetime
import threading
import time
import os
import mod_config
import ast
users = ast.literal_eval(mod_config.getConfig("userinfo","users"))
pw = ast.literal_eval(mod_config.getConfig("userinfo","pw"))
#确定用户名和密码
#users=["31902253","31902251","31902256","31902252","31902257","31902266","31902255","31902254","31802035"
#pw=["21003X","158172","270656","010479","126192","140015","290032","28691X","110044"]

#打卡部分
#判断是否完成打卡
def fun(b):
    time.sleep(2)
    bucket_text = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[2]/div/div/a[1]/div[2]/p[2]').get_attribute('textContent')
    ca="今日已打卡"
    if (bucket_text == ca):
        driver.quit()
        print(b)
        print("今日已打卡")
#打卡
    else:
        driver.get("http://ca.zucc.edu.cn/cas/login?service=http://yqdj.zucc.edu.cn/feiyan_api/h5/html/daka/daka.html")
        time.sleep(3)
#Q2
        driver.find_element_by_xpath('//*[@id="question-form"]/ul/li[2]/div[2]/div').click()
        #driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[1]').click()
        time.sleep(3)
        driver.find_element_by_class_name("btn-pickercity-ok").click()
        #driver.find_element_by_xpath('/html/body/div[4]/header/button[2]').click()
#Q3
        driver.find_element_by_xpath('//*[@id="question-form"]/ul/li[3]/div[2]/div/div/li[2]/label').click()
#Q4
        driver.find_element_by_xpath('//*[@id="question-form"]/ul/li[4]/div[2]/div/div/li[2]/label').click()
#Q5
        driver.find_element_by_xpath('//*[@id="question-form"]/ul/li[5]/div[2]/div/div/li[2]/label').click()
#Q6
        driver.find_element_by_xpath('//*[@id="question-form"]/ul/li[6]/div[2]/div/div/li[2]/label').click()
#Q8
        driver.find_element_by_xpath('//*[@id="question-form"]/ul/li[8]/div[2]/div/div/li[2]/label').click()
#Q10
        driver.find_element_by_xpath('//*[@id="question-form"]/ul/li[10]/div[2]/div/div/li[2]/label').click()
#Q11
        driver.find_element_by_xpath('//*[@id="question-form"]/ul/li[11]/div[2]/div/div/li[2]/label').click()
#Q12
        driver.find_element_by_xpath('//*[@id="question-form"]/ul/li[12]/div[2]/div/div/li[2]/label').click()
#Q13
        driver.find_element_by_xpath('//*[@id="question-form"]/ul/li[13]/div[2]/div/div/li[2]/label').click()
#Q14
        driver.find_element_by_xpath('//*[@id="question-form"]/ul/li[14]/div[2]/div/div/li[2]/label').click()
#Q15
        driver.find_element_by_xpath('//*[@id="question-form"]/ul/li[15]/div[2]/div/div/li[1]/label').click()
#Q16
        driver.find_element_by_xpath('//*[@id="question-form"]/ul/li[16]/div[2]/div/div/li[2]/label').click()
#Q17
       # driver.find_element_by_xpath('//*[@id="question-form"]/ul/li[17]/div[2]/div/div/li[2]/label').click()
        time.sleep(2)
#driver.find_element_by_xpath('//*[@id="page-1600880900637"]/div/div[4]/div[3]/a').click()
        driver.find_element_by_class_name("btn-commit").click()
# 退出
        driver.quit()
        print(b)
        print("打卡成功")

#主要部分
a=len(users)
for i in range(0,a):
    driver = webdriver.Chrome("./win/chromedriver") 
# linux 
    # driver = webdriver.Chrome("./linux/chromedriver")
# mac
    # driver = webdriver.Chrome("./mac/chromedriver")
    driver.get("http://yqdj.zucc.edu.cn/feiyan_api/h5/html/index/studentIndex.html")
    driver.find_element_by_id("username").send_keys(users[i])
    driver.find_element_by_id("password").send_keys(pw[i])
    driver.find_element_by_class_name("btn-submit").click()
    fun(users[i])
    driver.quit
print("全部打卡完成")

