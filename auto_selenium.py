import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

# driver_path = r"C:\Program Files (x86)\geckodriver.exe"
driver = webdriver.Firefox()

email = "mikkurds94@gmail.com"
password = "rdsrdsra"

# Go to linkedin and login
driver.get('https://www.linkedin.com/login')
time.sleep(3)
driver.find_element('id', 'username').send_keys(email)
driver.find_element('id', 'password').send_keys(password)
driver.find_element('id', 'password').send_keys(Keys.RETURN)
time.sleep(30)
# driver.find_element('id', 'ember44').send_keys(Keys.RETURN)
# WebDriverWait(driver, 2).until(EC.presence_of_element_located(('xpath', "//button[@id='ember235")))
# box_post = driver.find_element('x_path', "//button[@id='ember44']")
driver.find_element('xpath', "//button[@id='ember45']").click()
# box_post.click()
time.sleep(20)

modal = driver.find_element('class name', 'ql-editor')
post_reader = open("content.txt", "r")
post = post_reader.read()

modal.send_keys(post)

time.sleep(30)
# driver.find_element('xpath', "//button[@class='share-promoted-detour-button']").click()
driver.find_element('xpath', "//button[@id='ember221']").click()
time.sleep(10)
driver.quit()
print("Post Successfully DONE!!!")