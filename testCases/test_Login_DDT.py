import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import InvalidSessionIdException

from pageObjects.pageLogin import pageLogin
from utitlities.readProperties import readConfig
from utitlities.customLogger import LogGen
from utitlities import XLUtils


class Test_002_DDT_Login:
    baseURL = readConfig.getApplicationURL()
    path = './/testData/LoginTestDDT.xlsx'
    sheet = 'Sheet1'
    logger = LogGen.LogGeneration()

    def test_LoginAction(self,setup):
        self.logger.info("******************************test_LoginActio Initialize*************************")
        self.driver = setup
        self.logger.info("******************************Opening URL*************************************** ")
        self.driver.get(self.baseURL)
        self.loginPage = pageLogin(self.driver)
        self.driver.maximize_window()

        self.rows = XLUtils.getrowcount(self.path, self.sheet)
        print("Number of Rows = ", self.rows)
        lst_status=[]

        for r in range(2, self.rows+1):
            self.username = XLUtils.readData(self.path, self.sheet, r,1)
            self.password  = XLUtils.readData(self.path, self.sheet, r, 2)
            self.exp = XLUtils.readData(self.path, self.sheet,r, 3)

            self.loginPage.loginEmail(self.username)
            self.loginPage.loginPassword(self.password)
            self.loginPage.loginClick()
            time.sleep(20)

            pageTitle = self.driver.title
            expTitle = "Dashboard / nopCommerce administration"

            if pageTitle == expTitle:
                if self.exp == 'Pass':
                   self.logger.info('****************** Passed **********************')
                   self.loginPage.logoutClick()
                   lst_status.append("Pass")
                elif self.exp == 'Fail':
                   self.logger.error('****************** Failed **********************')
                   lst_status.append("Fail")

            elif pageTitle != expTitle:
                if self.exp == 'Pass':
                    self.logger.error('****************** Failed **********************')
                    self.loginPage.logoutClick()
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                  self.logger.info('****************** Passed **********************')
                  lst_status.append("Pass")
            print(lst_status)

        if "Fail" not in lst_status:
            self.logger.info("******************DDT Login Test Passed****************")
            self.driver.close()
            assert True

        else:
            self.logger.info("******************DDT Login Test Failed****************")
            self.driver.close()
            assert False

        self.logger.info("**************DDT Login Test Completed***********************")
        self.logger.info("***************Test_002_DDT_Login Completed ***************** ")

