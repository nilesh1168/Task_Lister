import time
from tests import driver, session


def changePassword():
    session.start()

    session.login()
    time.sleep(2)
    #After Login

    driver.find_element_by_id("user").click()
    time.sleep(1)
    driver.find_element_by_id("profset").click()
    time.sleep(1)

    driver.find_element_by_id("old_pass").send_keys("nil")
    time.sleep(1)
    driver.find_element_by_id("new_pass").send_keys("nilesh")
    time.sleep(1)
    driver.find_element_by_id("rep_new_pass").send_keys("niles")
    time.sleep(1)

    driver.find_element_by_id("submit").click()
    time.sleep(3)

    driver.refresh()

    driver.find_element_by_id("old_pass").send_keys("nil")
    time.sleep(1)
    driver.find_element_by_id("new_pass").send_keys("nilesh")
    time.sleep(1)
    driver.find_element_by_id("rep_new_pass").send_keys("nilesh")
    time.sleep(1)

    driver.find_element_by_id("submit").click()
    time.sleep(3)

    #logout
    session.logout()
    time.sleep(3)
    session.end()

changePassword()