from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time
from datetime import datetime

driver = webdriver.Chrome('driver/chromedriver') 

driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 600)

def getMessage():
    msg_path = '//*[contains(concat( " ", @class, " " ), concat( " ", "message-in", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "_3zb-j", " " ))]'
    all_mssgs = driver.find_elements_by_xpath(msg_path)
    lm = all_mssgs[-1]
    sendMessage(lm.text)

def sendMessage(mssg):
    inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@dir="ltr"][@data-tab="1"]'
    input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
    mssg = "Thank you for texting. I will reach u soon."
    input_box.send_keys(mssg + Keys.ENTER)

def replyTarget(target):
    x_arg = '//span[contains(@title,' + target + ')]'
    print(x_arg)
    group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
    print("Here-1")
    group_title.click()
    print("Clicked")
    getMessage()

def getTarget():
    path = '//div[@class="_3j7s9"]'
    all_chats = driver.find_elements_by_xpath(path)
    for chat in all_chats:
        try:
            chat.find_element_by_class_name("OUeyt")
            target_element = chat.find_element_by_class_name("_3TEwt")
            target = "'" + target_element.text+"'"
            print(target)
            replyTarget(target)
        except:
            continue
    time.sleep(1)
    getTarget()
time.sleep(5)
getTarget()