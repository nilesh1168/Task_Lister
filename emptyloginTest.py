import time
from tests import driver, session

def emptyLogin():
    session.start()
    time.sleep(2)
    #Login
    driver.find_element_by_name("login").click()
    time.sleep(1)
    driver.find_element_by_name("username").send_keys("")
    time.sleep(1)
    driver.find_element_by_id("password").send_keys("")
    time.sleep(1)
    driver.find_element_by_id("submit").click()

    time.sleep(1)
    session.end()

emptyLogin()