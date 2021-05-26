from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

import time
from datetime import date, timedelta

user = input ("Enter User name: ")
password = input ("Enter password: ")

url = "https://booking.chandigarhgolfclub.in/"

options = webdriver.ChromeOptions()
options.add_argument('--headless')

webdriver_path = r'C:/Users/harshvardhans/chromedriver.exe'
driver = webdriver.Chrome(webdriver_path, options=options)

driver.get(url)
driver.find_element_by_id("UserName_R").send_keys(user)
driver.find_element_by_id ("Password_R").send_keys(password)
driver.find_element_by_xpath('''//*[@id="LoginForm"]/p[2]/button''').click()

driver.get("https://booking.chandigarhgolfclub.in/index.php?m=account&v=Booking&timeterm=A&stdt=2020-11-11")
driver.find_element_by_xpath("/html/body/section[1]/section/div/section/div/div/div[2]/div[1]/div/ul/li[34]/label/span[2]").click()

fastrack = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '''//*[@id="select2-UserID_2-container"]''')))
fastrack.click()

x = driver.find_element_by_xpath("/html/body/span/span/span[1]/input")
x.send_keys("8172")
time.sleep(1)
x.send_keys(Keys.ENTER)

fastrack = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '''//*[@id="select2-UserID_3-container"]/span''')))
fastrack.click()

x = driver.find_element_by_xpath("/html/body/span/span/span[1]/input")
x.send_keys("8104")
time.sleep(1)
x.send_keys(Keys.ENTER)


driver.find_element_by_xpath('''//*[@id="DivCreateBooking"]/div[2]/div[2]/div/table/tfoot/tr/td/button''').click()
driver.quit()
