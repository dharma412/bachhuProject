import pytest

from selenium.webdriver import Firefox,Chrome

def get_driver_instance():
    browserType=pytest.config.option.browser
    #url=pytest.config.option.browser
    env=pytest.config.option.env
    if env=="local":
        if browserType=="Firefox":
            browser=Firefox
        elif browserType=="Chrome":
            browser=Chrome("C:/Users/Debasis/PycharmProjects/ApiSampleProject/browser_server/chromedriver.exe")
    else:
        print("Invalid Browser")
    browser.maximize_window()
    browser.implicitly_wait(30)
