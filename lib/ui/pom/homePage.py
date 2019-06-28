from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
class HomePage():
    def __init__(self, browser):
        self.browser=browser
        self.username="txtUsername"
        self.password="txtPassword"
        self.loginButton="btnLogin"
        self.errorMasg="//span[contains(text(),'Invalid credentials')"
    '''def wait_for_loginPage(self):
        wait=WebDriverWait(self.browser,30)
        wait.until(expected_conditions.visibility_of(self.find_element_by_id("frmLogin")))'''

    def get_user_name(self):
        try:
            return self.browser.find_element_by_id(self.username)
        except:
            return None

    def get_user_passwor(self):
        try:
            return self.browser.find_element_by_id(self.password)
        except:
            return None

    def get_user_loginButton(self):
        try:
            return self.browser.find_element_by_id(self.loginButton)
        except:
            return None

    def get_error_msg(self):
        try:
            return self.browser.find_element_by_xpath(self.errorMasg)
        except:
            return None
