import os, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# get the path of ChromeDriverServer
dir = os.path.dirname(__file__)
chrome_driver_path = dir + "\chromedriver"

# create a new Chrome session
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.maximize_window()
driver.implicitly_wait(50)


# Navigate to the application home page
driver.get("http://nileshs.pythonanywhere.com/")

time.sleep(3)
#Register
driver.find_element_by_name("register").click()

username = driver.find_element_by_name("username")
username.send_keys("")

driver.find_element_by_name("email").send_keys("")
time.sleep(1)
driver.find_element_by_name("password").send_keys("")
time.sleep(1)
driver.find_element_by_name("password2").send_keys("")

time.sleep(3)

driver.find_element_by_name("submit").click()

time.sleep(3)
driver.implicitly_wait(100)
# close the browser window
driver.quit()