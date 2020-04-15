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

target = '"Mehuli Pal Bon"'

string = "Hi this is a testing whatsapp bot. Please ignore the messages."

x_arg = '//span[contains(@title,' + target + ')]'
print(x_arg)
group_title = wait.until(EC.presence_of_element_located(( 
	By.XPATH, x_arg))) 
group_title.click() 
inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@dir="ltr"][@data-tab="1"]'
input_box = wait.until(EC.presence_of_element_located(( 
	By.XPATH, inp_xpath))) 
for i in range(50):
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	strs = string + "--" + str(i + 1) + current_time
	input_box.send_keys(strs + Keys.ENTER)
	time.sleep(1) 
