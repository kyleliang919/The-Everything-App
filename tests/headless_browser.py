import time
import random
import warnings
import undetected_chromedriver as uc


# initializing webdriver for Chrome
driver = uc.Chrome()
  
# getting GeekForGeeks webpage
driver.get('https://chat.openai.com/chat')

# setting a loop of headless browser
while True:
    cmd = input("what is your command?")
    if cmd == "exit":
        driver.close()
        exit()
    else:
        try:
            exec(cmd)
        except Exception as e: 
            print(e)

#driver.find_element("tag name", "textarea")[0].send_keys("hello")
#driver.find_elements("xpath", "/html/body/div/div/div/main/div[2]/form/div/div[2]/button")[0].click()
