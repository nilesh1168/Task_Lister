import time
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.maximize_window()
driver.implicitly_wait(4)

driver.get("http://nileshs.pythonanywhere.com/")

time.sleep(2)
#Login
driver.find_element_by_name("login").click()
time.sleep(1)
driver.find_element_by_name("username").send_keys("Nilesh")
time.sleep(1)
driver.find_element_by_id("password").send_keys("nilesh")

time.sleep(1)

driver.find_element_by_id("submit").click()

time.sleep(4)

#After Login

driver.find_element_by_id("user").click()
time.sleep(1)
driver.find_element_by_id("mytasks").click()
time.sleep(1)


driver.find_element_by_name("3").click()

#logout
driver.find_element_by_id("user").click()
time.sleep(1)
driver.find_element_by_id("logout").click()

time.sleep(3)

driver.quit()