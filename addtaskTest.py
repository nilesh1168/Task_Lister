import time
from tests import driver , session

def addTask():
    session.start()
    time.sleep(2)
    #Login 
    session.login()
    time.sleep(2)
    #After Login add tasks
    driver.find_element_by_id("user").click()
    time.sleep(1)
    driver.find_element_by_id("mytasks").click()
    time.sleep(1)
    driver.find_element_by_id("addtask").click()
    time.sleep(2)
    driver.find_element_by_name("t_head").send_keys("Random")
    time.sleep(1)
    driver.find_element_by_name("t_body").send_keys("Added task by Random ")
    time.sleep(1)
    driver.find_element_by_id("ddate").send_keys("18/10/2019")
    time.sleep(1)
    driver.find_element_by_id("submit").click()
    time.sleep(1)
    #logout
    session.logout()
    time.sleep(2)
    session.end()

addTask()    