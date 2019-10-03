import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# create a new Chrome session
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.maximize_window()
driver.implicitly_wait(50)


# Navigate to the application home page
driver.get("http://nileshs.pythonanywhere.com/")

time.sleep(3)
#Register Fail
driver.find_element_by_name("register").click()

username = driver.find_element_by_name("username")
username.send_keys("John Doe")

driver.find_element_by_name("email").send_keys("john")
time.sleep(1)
driver.find_element_by_name("password").send_keys("john")
time.sleep(1)
driver.find_element_by_name("password2").send_keys("doe")

time.sleep(3)

driver.find_element_by_name("submit").click()

time.sleep(3)
driver.implicitly_wait(100)
# close the browser window
driver.quit()