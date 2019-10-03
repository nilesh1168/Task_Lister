import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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

#After Login add tasks

driver.find_element_by_id("user").click()
time.sleep(1)
driver.find_element_by_id("mytasks").click()
time.sleep(1)

driver.find_element_by_id("addtask").click()
time.sleep(2)

driver.find_element_by_name("t_head").send_keys("Chaitanya")
time.sleep(1)
driver.find_element_by_name("t_body").send_keys("Added task by Chaitanya ")
time.sleep(1)
driver.find_element_by_id("ddate").send_keys("18/10/2019")
time.sleep(1)
driver.find_element_by_id("submit").click()
time.sleep(1)


#logout
driver.find_element_by_id("user").click()
time.sleep(1)
driver.find_element_by_id("logout").click()


time.sleep(2)
driver.quit()