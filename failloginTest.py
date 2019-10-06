import time
from tests import driver, session

def failLogin():
    session.start()
    time.sleep(2)
    #Login Fail
    driver.find_element_by_name("login").click()
    time.sleep(1)
    driver.find_element_by_name("username").send_keys("John Doe")
    time.sleep(1)
    driver.find_element_by_id("password").send_keys("john@123")
    time.sleep(1)
    driver.find_element_by_id("submit").click()

    time.sleep(2)
    session.end()

failLogin()