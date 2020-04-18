# The following script has been developed by Amartya Mondal.
# For more details visit https://atm1504.in
# Follow me at https://github.com/atm1504
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
target = '"Ashish Anjan"'

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

def getMessage(last_mssg):
    msg_path = '//*[contains(concat( " ", @class, " " ), concat( " ", "message-in", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "_3zb-j", " " ))]'
    all_mssgs = driver.find_elements_by_xpath(msg_path)
    lm = all_mssgs[-1]
    # Emoji will work only in Firefrox driver. Chrome web driver doesnot support emojis
    # emojis = lm.find_elements_by_tag_name("img")
    if lm.text == "Stop":
        time.sleep(0.5)
        getMessage("Stop")
    if str(lm.text) != last_mssg :
        last_mssg = str(lm.text)
        emoji=""
        # if len(emojis) > 0:
        #     for x in emojis:
        #         print("yes", str(x.get_attribute("alt")))
        #         #emoji += str(x.get_attribute("src"))
        #         emoji += str(x.get_attribute("alt"))
        sendMessage(last_mssg + emoji)
    time.sleep(0.5)
    getMessage(last_mssg)
print("ON")
time.sleep(5)  # time to load contents
getMessage("")