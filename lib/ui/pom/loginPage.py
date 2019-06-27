from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class LoginPage():
    def __init__(self, browser):
        self.browser=browser
    '''def wait_for_loginPage(self):
        wait=WebDriverWait(self.browser,30)
        wait.until(expected_conditions.visibility_of(self.find_element_by_id("facebook")))'''

    def get_user_name(self):
        try:
            return self.browser.find_element_by_id("email")
        except:
            return None

    def get_user_passwor(self):
        try:
            return self.browser.find_element_by_id("pass")
        except:
            return None

    def get_user_loginButton(self):
        try:
            return self.browser.find_element_by_xpath("//input[@type='submit']")
        except:
            return None

    def get_error_msg(self):
        try:
            return self.browser.find_element_by_xpath("//*[@id='globalContainer']/div[3]/div/div/div/text()")
        except:
            return None

