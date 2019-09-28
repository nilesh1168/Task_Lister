import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.maximize_window()
driver.implicitly_wait(4)

driver.get("http://127.0.0.1:5000/")

time.sleep(2)

driver.find_element_by_name("login").click()
time.sleep(1)
driver.find_element_by_name("username").send_keys("Nilesh")
time.sleep(1)
driver.find_element_by_id("password").send_keys("nil")

time.sleep(1)

driver.find_element_by_id("submit").click()

time.sleep(4)

#After Login

driver.find_element_by_id("user").click()
time.sleep(1)
driver.find_element_by_id("profset").click()
time.sleep(1)

driver.find_element_by_id("old_pass").send_keys("nil")
time.sleep(1)
driver.find_element_by_id("new_pass").send_keys("nilesh")
time.sleep(1)
driver.find_element_by_id("rep_new_pass").send_keys("niles")
time.sleep(1)

driver.find_element_by_id("submit").click()
time.sleep(3)

driver.refresh()

driver.find_element_by_id("old_pass").send_keys("nil")
time.sleep(1)
driver.find_element_by_id("new_pass").send_keys("nilesh")
time.sleep(1)
driver.find_element_by_id("rep_new_pass").send_keys("nilesh")
time.sleep(1)

driver.find_element_by_id("submit").click()
time.sleep(3)

driver.implicitly_wait(5)

driver.quit()