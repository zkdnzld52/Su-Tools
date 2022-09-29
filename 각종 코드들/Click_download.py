import requests
from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


path ="C:\workspace\chromedriver.exe"
driver = webdriver.Chrome(path)
a = 0
ran = 5743
# 5742번 까지 다운로드 받았음 / 9월 22일 09:40
ran2 = ran+10
for i in range(ran,ran2):
    variable = driver.current_url
    try:
        path = "http://106.255.230.162:13571/transcription/"+str(i)
        driver.get(path)
        time.sleep(1)
        if driver.current_url == "http://106.255.230.162:13571/transcription/1":
            continue
        else:
            driver.find_element(By.XPATH,'//*[@id="download-work"]/p').click()
            print(i,"번 다운로드")
            a+=1
            if i == ran2-1:
                print("마지막 다운")
                time.sleep(2)
        
            
    except:
        continue

print(a)