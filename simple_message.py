#Copyright@Souhardya & Amartya.
# For more details visit https://atm1504.in
# Follow me at https://github.com/atm1504
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time
from datetime import datetime

driver = webdriver.Chrome() 

driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 600) 

target = '"Target Name"'

string = "Hi this is a testing whatsapp bot. Please ignore the messages."

x_arg = '//span[contains(@title,' + target + ')]'
print(x_arg)
group_title = wait.until(EC.presence_of_element_located(( 
	By.XPATH, x_arg))) 
group_title.click() 
inp_xpath='//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
input_box = wait.until(EC.presence_of_element_located(( 
	By.XPATH, inp_xpath))) 
#50 means 50 times
for i in range(50):
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	strs = string + "--" + str(i + 1) + current_time
	input_box.send_keys(strs + Keys.ENTER)
	time.sleep(1) 
