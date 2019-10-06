import time
from tests import driver, session

def failRegister():
    session.start()
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
    session.end()

failRegister()    