import time
from tests import driver, session


def successRegister():
    session.start()

    time.sleep(3)
    driver.find_element_by_name("register").click()
    username = driver.find_element_by_name("username")
    username.send_keys("Jane Doe")
    driver.find_element_by_name("email").send_keys("jane123@d.com")
    time.sleep(1)
    driver.find_element_by_name("password").send_keys("jane123")
    time.sleep(1)
    driver.find_element_by_name("password2").send_keys("jane123")
    time.sleep(3)
    driver.find_element_by_name("submit").click()
    time.sleep(3)

    session.end()

successRegister()