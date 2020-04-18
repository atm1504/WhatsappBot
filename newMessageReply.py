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
    base_mssg_path = '//*[contains(concat( " ", @class, " " ), concat( " ", "message-in", " " ))]'
    all_mssgs = driver.find_elements_by_xpath(base_mssg_path)
    lm = all_mssgs[-1]
    mssg_text = lm.text.split("\n")
    try:
        replied = lm.find_element_by_class_name("_3FXB1")
        if str(replied.text) != "You · Status":
            raise Exception("Not status")
        lm_text = "Thank you for replying to my status."
        print("Is status")
    except:
        print("Is not status")
        print(mssg_text)
        lm_text = ""
        if len(mssg_text) > 2:
            if mssg_text[0] != "You":
                lm_text += "Hey " + mssg_text[0]
            lm_text += mssg_text[2]
        else:
            lm_text += mssg_text[0]
    sendMessage(lm_text)

def sendMessage(mssg):
    inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@dir="ltr"][@data-tab="1"]'
    input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
    # mssg = "Thank you for texting. I will reach u soon."
    input_box.send_keys(mssg + Keys.ENTER)
    print(mssg)

def replyTarget(target):
    x_arg = '//span[contains(@title,' + target + ')]'
    print(x_arg)
    group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
    group_title.click()
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