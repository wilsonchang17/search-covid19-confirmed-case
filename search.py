from selenium import webdriver
from selenium.webdriver.support.ui import Select
import datetime
import matplotlib.pyplot as plt
import urllib.request
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import requests
from bs4 import BeautifulSoup

def find(arr):
    for i in range(0,len(arr)):
        if arr[len(arr)-2] == "病" and arr[len(arr)-1] == "例":#處理均為境外移入 新版
            j = 0
            while(1):
                if(arr[j]=='9' or arr[j]=='8' or arr[j]=='7' or arr[j]=='6' or arr[j]=='5' or arr[j]=='4' or arr[j]=='3' or arr[j]=='2' or arr[j]=='1' or arr[j]=='0'):
                    print(arr[j])
                    num5.append(arr[j])
                if arr[j] == "C":
                    return #因為不同日期用這個方法會list out of range，也因為這邊是處理只有境外移入所以可以直接結束這find()
                j += 1
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
        if arr[i]=="-" and  arr[i+1]=="1" and arr[i+2]=="9" and arr[i+3]=="本" and arr[i+4]=="土":
            j=i-7
            while(1):
                if(arr[j]=='9' or arr[j]=='8' or arr[j]=='7' or arr[j]=='6' or arr[j]=='5' or arr[j]=='4' or arr[j]=='3' or arr[j]=='2' or arr[j]=='1' or arr[j]=='0'):
                    num3.append(arr[j])
                else:
                    break
                j = j-1
        if arr[i]=="均" and  arr[i+1]=="為": #處理均為境外移入
            j = 0
            while(1):
                if(arr[j]=='9' or arr[j]=='8' or arr[j]=='7' or arr[j]=='6' or arr[j]=='5' or arr[j]=='4' or arr[j]=='3' or arr[j]=='2' or arr[j]=='1' or arr[j]=='0'):
                    num4.append(arr[j])
                if arr[j] == "C":
                    break
                j += 1
                



time_ = input("請輸入時間")
print("查詢日期為: ",time_)
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
num1 = [] #本土
num2 = [] #境外
num3 = [] #本土特殊情況
num4 = [] #均為境外移入
num5 = [] #均為境外移入 新版
num6 = [] #均為境外移入 包含國家

for i in data:
    if i.text[0] == '新' and i.text[1] == '增':
        arr = i.text
        find(arr)
    if i.text[2] == '中' and i.text[3] == '心' and i.text[4] == '公' and i.text[5] == '布':
        arr = i.text
        find(arr)
#print(num1)
#print(num2)
#print(num3)
#print(num4)
#print(num5)
if num3 == []:
    print("本土案例為: ",end = "")
    if num1 == []:
        print("0",end = "")
    else:
        for i in range(len(num1)-1,-1,-1):
            print(num1[i],end="")
else:      
    print("本土案例為: ",end = "")
    for i in range(len(num3)-1,-1,-1):
        print(num3[i],end="")

print()
print("境外移入為: ",end = "")
if num2 == []:
    if num4 != []:
        for i in range(len(num4)):
            print(num4[i],end="")
    elif num5 != []:
        for i in range(len(num5)):
            print(num5[i],end="")
    else:
        print("0")
else:
    for i in range(len(num2)-1,-1,-1):
        print(num2[i],end="")
        
        
        
