from selenium import webdriver
import unittest
import time
from SampleProjects.POMProjectDemo.Pages.LoginPage import LoginPage
from SampleProjects.POMProjectDemo.Pages.HomePage import HomePage
from SampleProjects.POMProjectDemo.Pages.CreateAnAccountPage import CreateAnAccountPage
from SampleProjects.POMProjectDemo.Pages.MyAccountPage import MyAccountPage
from SampleProjects.POMProjectDemo.Pages.PersonInfoPage import PersonalInfoPage
from SampleProjects.POMProjectDemo.Pages.MyAddressesPage import MyAddressesPage
from SampleProjects.POMProjectDemo.Pages.UpdateAddressPage import UpdateAddressPage


class EditInfoTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\\chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_editinfo(self):
        firstname = "XXX"
        lastname = "ZZZ"
        email = "POMtestgit1@testmail.com"
        oldpass = "123TEST"
        newpass = "123TEST"
        confirmation = "123TEST"
        day = "3"
        month = "August"
        year = "1994"
        company = "Colaqueen"
        address1 = "Mustafar Avenue, Hoth Street N 42"
        address2 = "Coruscant"
        city = "Central"
        state = "New York"
        postcode = "42421"
        country = "United States"
        addinfo = "wazzup"
        homephone = "+902121234567"
        mobilephone = "+905331112233"
        alias = "newaddress"

        driver = self.driver
        self.driver.get("http://automationpractice.com")
        time.sleep(2)

        loginpage = LoginPage(driver)
        homepage = HomePage(driver)
        createanaccountpage = CreateAnAccountPage(driver)
        myaccountpage = MyAccountPage(driver)
        personalinfopage = PersonalInfoPage(driver)
        myaddressespage = MyAddressesPage(driver)
        updateaddresspage = UpdateAddressPage(driver)

        homepage.enterto_accountpage()
        loginpage.enter_email("test1@testmail.com")
        loginpage.enter_password("123456789test")
        loginpage.signin()
        myaccountpage.goto_presonalinfo()
        personalinfopage.check_genderfemale()
        personalinfopage.check_subscriptions()
        personalinfopage.editinfo(firstname, lastname, email, day, month, year, oldpass, newpass, confirmation)
        personalinfopage.saveinfo()
        personalinfopage.backtoaccount()
        myaccountpage.goto_addresses()
        myaddressespage.addressupdate()
        updateaddresspage.updateaddress(firstname, lastname, company, address1, address2, city, state, postcode, country, addinfo, homephone, mobilephone,  alias)
        updateaddresspage.saveupdatedaddress()
        updateaddresspage.backtoaddresses()
        personalinfopage.backtoaccount()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test is completed!")
