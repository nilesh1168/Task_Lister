import time
from tests import driver , session

def successLogin():
    session.start()
    time.sleep(2)
    #login
    session.login()
    time.sleep(2)

    #logout
    session.logout()
    time.sleep(2)
    driver.quit()

successLogin()    