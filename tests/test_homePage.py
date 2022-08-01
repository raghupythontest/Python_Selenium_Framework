import time

import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.homePage import HomePage
from tests.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    # dataset = [
    #     {
    #         "firstName": "Raghuvaran",
    #         "email": "xyx@gmail.com",
    #         "password":"12345678",
    #         "gender": "Male"
    #     }
    #     ,
    #     {
    #         "firstName": "charan",
    #         "email": "charan@gmail.com",
    #         "password": "12345678",
    #         "gender": "Female"
    #     }
    # ]

    def testCaseForm(self, getData):
        log=self.getLogger()
        print(getData)
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")
        hp = HomePage(self.driver)
        hp.get_name_element().send_keys(getData["firstName"])
        hp.get_email_element().send_keys(getData["email"])
        hp.get_password_element().send_keys(getData["password"])
        hp.get_checkBox().click()

        self.selectByVisibleText(hp.get_dropdown(), getData["gender"])
        # gender = Select(hp.get_dropdown())
        # gender.select_by_index(0)
        hp.get_submitButton().click()
        message = hp.getAlertMessage().text
        # print(gender.all_selected_options)
        log.info(message)
        time.sleep(2)
        # driver.find_element(By.XPATH, "//input[@name='name']").send_keys("Raghuvaran")
        # driver.find_element(By.NAME, "email").send_keys("xyz@gmail.com")
        # driver.find_element(By.CSS_SELECTOR, "#exampleInputPassword1").send_keys("12345678")
        # driver.find_element(By.ID, "exampleCheck1").click()
        # driver.find_element(By.XPATH, "//input[@type='submit']").click()
        log.info(message)
        assert "Success" in message

    @pytest.fixture(params=HomePageData.getDataSet("Testcase3"))
    def getData(self, request):
        return request.param
