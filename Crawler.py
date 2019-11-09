#author: wr786
#-*- coding:utf-8 -*- 
import requests
import os
import re
import codecs
from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')

abspath = os.path.abspath(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
browser = webdriver.Chrome(abspath)
url = r'http://162.105.86.10/programming/'
url2 = input("请输入您想要archive的题集的url:\n")

browser.get(url)
# 等待js脚本加载完毕
browser.implicitly_wait(5)

usr = input("请输入您的用户名:")
psw = input("请输入您的密码(口令):")

username = browser.find_element_by_xpath('//*[@id="username"]')
username.send_keys(usr)
password = browser.find_element_by_xpath('//*[@id="password"]')
password.send_keys(psw)

browser.implicitly_wait(3)

login_button = browser.find_element_by_id('login')
login_button.click()

browser.implicitly_wait(3)

browser.get(url2)
data = browser.page_source.encode('UTF-8').decode()

#pattern = re.compile(r'<a href="(.*?)"><font color="green">通过</font></a>')
pattern = re.compile(r'<a href="(.*?)"><font color="green">通过</font></a>')
problems = re.findall(pattern, data)

for problem in problems:
    url_problem = r'http://162.105.86.10' + problem

    browser.get(url_problem)
    data_problem = browser.page_source.encode('UTF-8').decode()
    pattern_submit = re.compile(r'<a href="(.*?)"><font color="blue">Passed</font>')
    submits = re.findall(pattern_submit, data_problem)
    url_code = r'http://162.105.86.10' + submits[0] + r'&sourceCode=true'

    browser.get(url_code)
    data_code = browser.page_source.encode('UTF-8').decode()
    pattern_title = re.compile(r'title="题目:(.*?)" style="text-decoration: none;">')

    title = re.findall(pattern_title, data_code)
    pos1 = data_code.find("<code>")
    pos2 = data_code.find("</code>")
    archive = data_code[pos1+6:pos2]
    pos3 = archive.find('*/')
    # 细节处理
    archive = archive[pos3+2:] # 去除开头注释
    archive = archive.replace("&lt;", '<') # replace竟然不会改变原字符串的内容！！！
    archive = archive.replace("&gt;", '>')

    file_path = os.path.join(os.path.abspath('.'), 'output', title[0] + '.cpp')
    f = codecs.open(file_path, 'w', 'utf-8')
    f.write(archive)
    f.close()

browser.quit()

print("Position Zero!")