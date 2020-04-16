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

target = '"_amartya_"'

string = "Hi this is a testing whatsapp bot. Please ignore the messages."

x_arg = '//span[contains(@title,' + target + ')]'
print(x_arg)
group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
group_title.click()

status_path='//div[@class="_3sgkv Gd51Q"]'
time.sleep(5)
visibility_off_stat = []
# Last seen visibility on
def statVisibilityOn():
    stat = []
    n = len(stat)
    while True:
        try:
            status_data = wait.until(EC.presence_of_element_located((By.XPATH, status_path)))
            status = status_data.text
            if status == "online" and len(stat) > 0 and ("online" not in str(stat[-1])):
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                stat.append("online" + " - " + dt_string)
                print(stat[-1])
            elif status == "online" and len(stat)==0:
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                stat.append("online" + " - " + dt_string)
                print(stat[-1])
            elif stat != "online" and len(stat) > 0 and stat[-1] != status:
                stat.append(status)
                print(stat[-1])
            elif stat != "online" and len(stat) == 0:
                stat.append(status)
                print(stat[-1])
        except:
            print("Error occured")
            time.sleep(2)


# Last seen visibility off
def statVisibilityOff(count):
    stat = []
    n = len(stat)
    count = 0
    flag = 0
    while True:
        try:
            status_data = wait.until(EC.presence_of_element_located((By.XPATH, status_path)))
            status = status_data.text
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            millis = int(round(time.time() * 1000))
            t = "Online at - " + dt_string
            if flag == 1 and millis - stat[-1][1] >= 10000:
                stat.append([t, millis])
                print(stat[-1])
            elif flag == 1:
                stat[-1][1] = millis
            elif flag == 0:
                stat.append([t, millis])
                flag = 1
                print(stat[-1])
            time.sleep(2)
        except:
            print("Error occured")
            break

userType = input("Press 1 if last seen is visible else press 0: ")
if userType == "1":
    statVisibilityOn()
else:
    statVisibilityOff(1)