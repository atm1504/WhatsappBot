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

# Target user
target = "_amartya_"

time.sleep(10) # time to load the page
x_arg = '//span[contains(@title,' + "'" + target + "'" + ')]'
print(x_arg)
group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
group_title.click()

def sendMessage(mssg):
    inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@dir="ltr"][@data-tab="1"]'
    input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
    input_box.send_keys(mssg + Keys.ENTER)

def getMessage(last_mssg):
    base_mssg_path = '//*[contains(concat( " ", @class, " " ), concat( " ", "message-in", " " ))]'
    all_mssgs = driver.find_elements_by_xpath(base_mssg_path)
    lm = all_mssgs[-1]
    mssg_text = lm.text.split("\n")
    print(mssg_text)
    try:
        replied = lm.find_element_by_class_name("_3FXB1")
        if str(replied.text) != "You · Status":
            raise Exception("Not status")
        lm_text = "Thank you for replying to my status."
    except:
        n = len(mssg_text)
        if n ==4:
            lm_text = mssg_text[2]
        elif n == 3 or n == 1:
            lm_text = "Sorry emoji not supported"
        else:
            lm_text = mssg_text[0]
    if lm_text == last_mssg:
        time.sleep(1)
        getMessage(last_mssg)
    sendMessage(lm_text)
    time.sleep(1)
    getMessage(lm_text)
print("ON")
time.sleep(5)  # time to load contents
getMessage("")