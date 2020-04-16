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
target = '"Sayantan Banerjee"'

time.sleep(10) # time to load the page
x_arg = '//span[contains(@title,' + target + ')]'
print(x_arg)
group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
group_title.click()

def sendMessage(mssg):
    inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@dir="ltr"][@data-tab="1"]'
    input_box = wait.until(EC.presence_of_element_located(( 
        By.XPATH, inp_xpath)))
    input_box.send_keys(mssg + Keys.ENTER)

def getMessage():
    msg_path = '//div[@class="_3zb-j"]//span[@class="_3FXB1 selectable-text invisible-space copyable-text"]'
    all_mssgs = driver.find_elements_by_xpath(msg_path)
    a = all_mssgs[-1].text
    # b = all_mssgs[-2].text
    if a[0] != "$":
        mssg = "$You said - " + str(a)
        sendMessage(mssg)
    time.sleep(1)
    getMessage()

print("ON")
time.sleep(5) # time to load contents
getMessage()