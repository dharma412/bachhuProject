from selenium.webdriver import Chrome
from lib.ui.pom.loginPage import LoginPage
import unittest
import time
class Test_login01(unittest.TestCase):
    def setUp(self):
        self.browser=Chrome("C://Users/Debasis/PycharmProjects/ApiSampleProject/browser_server/chromedriver.exe")
        self.browser.implicitly_wait(20)
        self.browser.maximize_window()
        self.browser.get("https://www.facebook.com")
        self.login_page=LoginPage(self.browser)
    def tearDown(self):
        self.browser.close()

    def test_login_valid_tc01(self):
        #self.login_page.wait_for_loginPage()
        self.login_page.get_user_name().send_keys("")
        self.login_page.get_user_passwor().send_keys("")
        self.login_page.get_user_loginButton().click()
        actual_result=self.browser.title

        print(actual_result)
        self.assertEqual(self.browser.title,"(1) Facebook")
        self.browser.get_screenshot_as_file("")
if __name__=='main':
    unittest.main


