import time
from tests import driver, session

def delTask():
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
    driver.find_element_by_name("3").click()

    #logout
    session.logout()
    time.sleep(1)
    session.end()

delTask()    