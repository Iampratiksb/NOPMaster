import pytest
from selenium import webdriver
from pageObjects.pageLogin import pageLogin
from utitlities.readProperties import readConfig
from utitlities.customLogger import LogGen


class Test_001_Login:
    baseURL = readConfig.getApplicationURL()
    username = readConfig.getApplicationEmail()
    password = readConfig.getApplicationPassword()
    logger = LogGen.LogGeneration()

    def test_HomePageTitle(self,setup):
        self.logger.info("**************************Test_001_Login Started********************************")
        self.logger.info("**************************test_HomePageTitle Initialize*************************")
        self.driver = setup
        self.logger.info("******************************Opening URL*************************************** ")
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.logger.info("********************************test_HomePageTitle Passed *****************************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_HomePageTitle.png")
            self.logger.error("********************************test_HomePageTitle Failed *****************************")
            self.driver.close()
            assert False


    def test_LoginAction(self,setup):
        self.logger.info("******************************test_LoginActio Initialize*************************")
        self.driver = setup
        self.logger.info("******************************Opening URL*************************************** ")
        self.driver.get(self.baseURL)
        self.loginPage = pageLogin(self.driver)
        self.loginPage.loginEmail(self.username)
        self.loginPage.loginPassword(self.password)
        self.loginPage.loginClick()
        pageTitle = self.driver.title

        if pageTitle == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("********************************test_LoginAction Passed *****************************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_LoginAction.png")
            self.logger.error("********************************test_LoginAction Failed *****************************")
            self.driver.close()
            assert False

