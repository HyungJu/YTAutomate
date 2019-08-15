def getUsers(account):
    from  selenium import webdriver
    import time

    import selenium.webdriver.chrome.service as service
    from selenium.webdriver.common.keys import Keys
    import json


    
    options = webdriver.ChromeOptions()

    # headless 옵션 설정
    options.add_argument("headless")
    options.add_argument("no-sandbox")

    # 브라우저 윈도우 사이즈
    options.add_argument('window-size=1920x1080')

    # 사람처럼 보이게 하는 옵션들
    options.add_argument("disable-gpu")   # 가속 사용 x
    options.add_argument("lang=ko_KR")    # 가짜 플러그인 탑재
    options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 이름 설정





    driver = webdriver.Chrome('/home/hyungju/chromedriver')
    driver.get('https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Dko%26next%3D%252F&hl=ko&flowName=GlifWebSignIn&flowEntry=ServiceLogin');
    driver.implicitly_wait(3) # Let the user actually see something!

    email_input = driver.find_element_by_xpath('//*[@id="identifierId"]')
    email_input.send_keys(account["email"])
    email_input.send_keys(Keys.ENTER)

    driver.implicitly_wait(3)

    pass_input = driver.find_element_by_name('password')

    pass_input.send_keys(account["password"])

    driver.implicitly_wait(3)
    pass_input.send_keys(Keys.ENTER)
    time.sleep(2)
    driver.get('https://families.google.com/u/0/families/create')
    #driver.quit()
    driver.implicitly_wait(3)

    user_list = []

    users = driver.find_elements_by_xpath('//*/c-wiz/div/div[2]/div[1]/div/div[1]/div[3]/div')
    i = 1
    for user in users :
        if(i>len(users)):
            break
        user.find_element_by_tag_name('div').send_keys(Keys.ENTER)
        driver.implicitly_wait(3)
        
        try :
            user_list.append(driver.find_element_by_xpath('//*/div['+str(7+i-1)+']/div/div[2]/span/c-wiz/div/div[1]/div/div/label/div[3]').text)
        except:
            pass
        i+=1
    return user_list
    driver.quit()


