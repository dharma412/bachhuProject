from selenium.webdriver import Chrome
from lib.ui.pom.homePage import HomePage
from selenium.common.exceptions import NoSuchElementException
#from lib.utils.mouseHover import moveToElement
import unittest

import pytest
import time
class Test_homePage01(unittest.TestCase):
    def setUp(self):
        self.browser=Chrome("C://Users/Debasis/PycharmProjects/ApiSampleProject/browser_server/chromedriver.exe")
        self.browser.implicitly_wait(20)
        self.browser.maximize_window()
        self.browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/validateCredentials")
        self.home_page=HomePage(self.browser)
    def tearDown(self):
        self.browser.get_screenshot_as_file("C:/Users/Debasis/PycharmProjects/ApiSampleProject/errorScreenshot"+self._testMethodName+"."+"png")
        self.browser.close()

    def test_homePage_valid_tc01(self):

        # self.home_page.wait_for_loginPage()
        self.home_page.get_user_name().send_keys("Admin")
        self.home_page.get_user_passwor().send_keys("admin123")
        self.home_page.get_user_loginButton().click()
        self.assertTrue(self.browser.title,'OrangeHRM')
    def test_homePage_logout(self):
        try:
            # self.home_page.wait_for_loginPage()
            self.home_page.get_user_name().send_keys("Admin")
            self.home_page.get_user_passwor().send_keys("admin123")
            self.home_page.get_user_loginButton().click()
            self.assertTrue(self.browser.title, 'OrangeHRM')
            self.browser.find_element_by_id("welcome").click
            self.browser.find_element_by_link_text("Logout").click()
            self.browser.get_screenshot_as_file("C:/Users/Debasis/PycharmProjects/ApiSampleProject/errorScreenshot/logOut.png")
            print("Logout Successful")
        except NoSuchElementException as e:
            print(e)


if __name__=='main':
    unittest.main()



