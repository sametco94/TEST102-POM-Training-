from selenium import webdriver
import unittest
import time
from SampleProjects.POMProjectDemo.Pages.LoginPage import LoginPage
from SampleProjects.POMProjectDemo.Pages.HomePage import HomePage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\\chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        driver.get("http://automationpractice.com")
        time.sleep(3)

        loginpage = LoginPage(driver)
        homepage = HomePage(driver)

        homepage.enterto_accountpage()
        loginpage.enter_email("POMtestgit1@testmail.com")
        loginpage.enter_password("123TEST")
        loginpage.signin()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed!")