import time
from tests import driver, session

def descTask():
    session.start()
    time.sleep(2)
    #Login
    session.login()
    time.sleep(2)
    #After Login
    driver.find_element_by_id("user").click()
    time.sleep(1)
    driver.find_element_by_id("mytasks").click()
    time.sleep(1)
    driver.find_element_by_id("2").click()
    time.sleep(1)
    #logout
    session.logout()
    time.sleep(3)
    session.end()

descTask()