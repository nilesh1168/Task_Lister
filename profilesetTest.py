import time
from tests import driver , session

def emptyChangePassword():
    session.start()
    time.sleep(2)
    #Login
    session.login()
    time.sleep(2)

    #After Login
    driver.find_element_by_id("user").click()
    time.sleep(1)
    driver.find_element_by_id("profset").click()
    time.sleep(1)

    driver.find_element_by_id("old_pass").send_keys("")
    time.sleep(1)
    driver.find_element_by_id("new_pass").send_keys("")
    time.sleep(1)
    driver.find_element_by_id("rep_new_pass").send_keys("")
    time.sleep(1)
    driver.find_element_by_id("submit").click()
    time.sleep(3)

    #logout
    session.logout()
    time.sleep(2)
    session.end()

emptyChangePassword()    