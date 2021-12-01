from selenium import webdriver
import unittest
import time
from SampleProjects.POMProjectDemo.Pages.LoginPage import LoginPage
from SampleProjects.POMProjectDemo.Pages.HomePage import HomePage
from SampleProjects.POMProjectDemo.Pages.CreateAnAccountPage import CreateAnAccountPage


class RegisterTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\\chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_register(self):
        gender = "male"
        firstname = "ABC"
        lastname = "DEF"
        newpass = "123TEST"
        day = "1"
        month = "September"
        year = "1994"
        company = "Colaking"
        address1 = "Mustafar Avenue, Hoth Street N 42"
        address2 = "Coruscant"
        city = "Central"
        state = "Wisconsin"
        postcode = "4242"
        country = "United States"
        addinfo = "wazzup"
        homephone = "+902121234567"
        mobilephone = "+905371112233"
        alias = "mainaddress"

        driver = self.driver
        self.driver.get("http://automationpractice.com")
        time.sleep(2)

        loginpage = LoginPage(driver)
        homepage = HomePage(driver)
        createanaccountpage = CreateAnAccountPage(driver)

        homepage.enterto_accountpage()
        loginpage.emailcreate("POMtestgit4@testmail.com")
        loginpage.goto_emailcreate()
        createanaccountpage.filltheinfo(firstname, lastname, newpass, day, month, year, company, address1, address2, city, state, postcode, country, addinfo, homephone, mobilephone, alias)

        if gender == "male":
            createanaccountpage.check_gendermale()
        else:
            createanaccountpage.check_genderfemale()

        createanaccountpage.check_subscriptions()
        createanaccountpage.submit_info()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test is completed!")
