# import TimeUnit as TimeUnit
import pytest
#import self as self
from selenium import webdriver

#from pageObjects.LoginPage import Login
import time

from selenium.webdriver.common.by import By


#from utilities.readProperties import ReadConfig
#from utilities.customLogger import LogGen



class TestLogin():
    baseURL = "https://carepossible-app-preprod.azurewebsites.net/"
    userName = "shilpa.s1602+1@jenesys.co"
    password = "Password1"

    textbox_username_id = "loginEmail"
    textbox_password_id = "loginPassword"
    button_login_xpath = "//*[@id='ember673']/form/div[3]/div/button"

    # Testcase 1: To verify the title of the page
    def test_homePageTitle(self):
        self.driver = webdriver.Chrome()
       # self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Help at home, your way - Care Possible":
           # self.logger.info("********** Home page title testcase is passed ****************88")
            self.driver.close()
            assert True


        else:
            #self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
           # self.logger.error("**********Home page title testcase is Failed***********")
            self.driver.close()
            assert False

    # Testcase2 - Verify login functionality
    def test_login(self):

        #self.logger.info("************Verifying test_login ************")


        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        time.sleep(10)
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(self.userName)
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(self.password)
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

        # self.driver.implicitly_wait(30)
        time.sleep(20)
        act_title = self.driver.title

        if act_title == "Help at home, your way - Care Possible":
            assert True
            #self.logger.info("********** Verify the Login test case is passed ***************")
            self.driver.close()

        else:
           # self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            assert False
           # self.logger.error("************* Verify the Login test case is failed **********888888")
            self.driver.close()

