import os, time
from tests import driver, session

def emptyRegister():
    session.start()
    time.sleep(2)
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
    session.end()

emptyRegister()