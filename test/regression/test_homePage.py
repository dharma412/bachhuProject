from selenium.webdriver import Chrome
from lib.ui.pom.homePage import HomePage
#from lib.utils.mouseHover import moveToElement
import unittest
import pytest
import time
class Test_homePage01(unittest.TestCase):
    def setUp(self):
        self.browser=Chrome("C:/Users/Debasis/PycharmProjects/ApiSampleProject/browser_server/chromedriver.exe")
        self.browser.implicitly_wait(20)
        self.browser.maximize_window()
        self.browser.get("https://www.facebook.com")
        self.home_page=HomePage(self.browser)
    def tearDown(self):
        self.browser.close()

    def test_homePage_valid_tc01(self):
        #self.login_page.wait_for_loginPage()
        self.home_page.get_user_name().send_keys("bachhunandi38@gmail.com")
        self.home_page.get_user_passwor().send_keys("electronices2#")
        self.home_page.get_user_loginButton().click()
        actual_result=self.browser.title

        print(actual_result)
        ex_msg="Facebook"
        self.assertTrue(self.browser.title,'Facebook')
        '''#self.browser.find_element_by_xpath("//div[@id='userNavigationLabel']").click
        #logout=self.browser.find_element_by_id("userNavigationLabel")
        #moveToElement(self.browser,logout)

        time.sleep(35)
        logout1=self.browser.find_element_by_partial_link_text("Log Out")
        logout1.click()


        #self.browser.find_element_by_partial_link_text('Log Out').click()'''




if __name__=='main':
    unittest.main()



