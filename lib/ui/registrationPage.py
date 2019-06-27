import unittest
from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException
from lib.utils import dropDown
import logging

class Test_login01(unittest.TestCase):
    def setUp(self):
        self.driver=Chrome("C:/Users/Debasis/PycharmProjects/ApiSampleProject/browser_server/chromedriver.exe")
        self.driver.get("https://www.facebook.com")
        self.driver.implicitly_wait(30)
    def test_birthday(self):
        day=self.driver.find_element_by_id("day")
        dropDown.selectByvalue(day,'25')
        month=self.driver.find_element_by_id("month")
        dropDown.selectByIndex(month,2)
        year=self.driver.find_element_by_id("year")
        dropDown.selectByVisibleText(year,'1991')
        logging.basicConfig(filename="C:/Users/Debasis/PycharmProjects/ApiSampleProject/logFile/test.log",
                            format='%(asctime)s:%(levelname)s:%(message)s',
                            datefmt='%m/%d/%y %I:%M:%S')
        loger=logging.getLogger()
        loger.setLevel(logging.DEBUG)
    def test_radio_button(self):
        self.driver.find_element_by_xpath("//input[@value='2']").click()
    def tearDown(self):
        self.driver.close()
