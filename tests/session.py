import time
from selenium import webdriver
from tests import driver

def start():
    driver.maximize_window()
    driver.implicitly_wait(4)
    driver.get("http://nileshs.pythonanywhere.com/")

def end():
    driver.quit()

def login():
    driver.find_element_by_name("login").click()
    time.sleep(1)
    driver.find_element_by_name("username").send_keys("Nilesh")
    time.sleep(1)
    driver.find_element_by_id("password").send_keys("nilesh")
    time.sleep(1)
    driver.find_element_by_id("submit").click()
        

def logout():
    driver.find_element_by_id("user").click()
    time.sleep(1)
    driver.find_element_by_id("logout").click()     