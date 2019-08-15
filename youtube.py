#!/usr/bin/python3

from  selenium import webdriver
import time

import selenium.webdriver.chrome.service as service
from selenium.webdriver.common.keys import Keys




options = webdriver.ChromeOptions()

# headless 옵션 설정
options.add_argument("no-sandbox")


# 사람처럼 보이게 하는 옵션들
options.add_argument("disable-gpu")   # 가속 사용 x
options.add_argument("lang=ko_KR")    # 가짜 플러그인 탑재
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 이름 설정




service = service.Service('chromedriver')
service.start()

driver = webdriver.Remote(service.service_url, options=options)
driver.get('https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Dko%26next%3D%252F&hl=ko&flowName=GlifWebSignIn&flowEntry=ServiceLogin');
time.sleep(1) # Let the user actually see something!

email_input = driver.find_element_by_xpath('//*[@id="identifierId"]')
email_input.send_keys('blackcowlatte')
email_input.send_keys(Keys.ENTER)

time.sleep(3)

pass_input = driver.find_element_by_name('password')
time.sleep(3)
pass_input.send_keys('youtubepremium')


pass_input.send_keys(Keys.ENTER)
time.sleep(3)
driver.get('https://families.google.com/u/0/families/invite')
#driver.quit()
time.sleep(10)


add_email = driver.find_element_by_xpath('//*[@placeholder="이름이나 이메일 주소를 입력하세요."]')
time.sleep(2)
add_email.send_keys('hello')
time.sleep(2)
add_email.send_keys(Keys.ENTER)
time.sleep(5)

family_add_btn = driver.find_element_by_xpath('//*/c-wiz/div/div[2]/div[1]/div/div[3]/div[1]').click()
time.sleep(5)
