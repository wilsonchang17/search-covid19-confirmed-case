from selenium import webdriver
from selenium.webdriver.support.ui import Select
import datetime
import matplotlib.pyplot as plt
import urllib.request
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import requests
from bs4 import BeautifulSoup

url = 'https://www.cdc.gov.tw/Bulletin/List/MmgtpeidAR5Ooai4-fgHzQ'
html = requests.get(url) 
html.encoding = 'utf8' 
sp = BeautifulSoup(html.text, 'lxml')

time_ = input("請輸入時間")
print(time_)
time_ = time_.replace("/",".")

option = webdriver.ChromeOptions()
option.add_argument("headless")
browser = webdriver.Chrome("D:\google download\chromedriver_win32 (1)\chromedriver.exe", options=option)
browser.get("https://www.cdc.gov.tw/Bulletin/List/MmgtpeidAR5Ooai4-fgHzQ")

elem = browser.find_element_by_xpath('//*[@id="startTime"]')
browser.find_element_by_xpath('//*[@id="startTime"]').click()
actions = ActionChains(browser)
actions.move_to_element(elem).click().send_keys(str(time_)).perform()

elem = browser.find_element_by_xpath('//*[@id="endTime"]')
browser.find_element_by_xpath('//*[@id="endTime"]').click()
actions = ActionChains(browser)
actions.move_to_element(elem).click().send_keys(str(time_)).perform()

browser.find_element_by_xpath('//*[@id="form"]/div/div[3]/button').click()


sp = BeautifulSoup(browser.page_source, 'lxml')
data = sp.find_all("p",class_ = "JQdotdotdot")
arr = ''
for i in data:
    if i.text[0] == '新' and i.text[1] == '增':
        arr = i.text

num1 = []
num2 = []
for i in range(0,len(arr)):
    if arr[i]=="例" and  arr[i+1]=="本" and arr[i+2]=="土":

        j=i-1
        while(1):
            if(arr[j]=='9' or arr[j]=='8' or arr[j]=='7' or arr[j]=='6' or arr[j]=='5' or arr[j]=='4' or arr[j]=='3' or arr[j]=='2' or arr[j]=='1' or arr[j]=='0'):
                num1.append(arr[j])
            else:
                break
            j = j-1
    if arr[i]=="例" and  arr[i+1]=="境" and arr[i+2]=="外":
        j=i-1
        while(1):
            if(arr[j]=='9' or arr[j]=='8' or arr[j]=='7' or arr[j]=='6' or arr[j]=='5' or arr[j]=='4' or arr[j]=='3' or arr[j]=='2' or arr[j]=='1' or arr[j]=='0'):
                num2.append(arr[j])
            else:
                break
            j = j-1

print("本土案例為: ",end = "")
if num1 == []:
    print("0",end = "")
else:
    for i in range(len(num1)-1,-1,-1):
        print(num1[i],end="")
print()
print("境外移入為: ",end = "")
if num2 == []:
    print("0")
else:
    for i in range(len(num2)-1,-1,-1):
        print(num2[i],end="")
