import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# @pytest.mark.usefixtures("setup")
from pageObjects.checkoutPage import CheckoutPage
from pageObjects.homePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        log=self.getLogger()
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")
        hp=HomePage(self.driver)
        cp=CheckoutPage(self.driver)
        hp.shop_nav().click()
        # self.driver.find_element(By.LINK_TEXT, "Shop").click()

        # all_products = self.driver.find_elements(By.CSS_SELECTOR, "div.card")
        all_products=cp.get_products()

        # name=input("Enter the product name :")
        name = "iphone"
        log.info("Product to be selected:"+name)

        for product in all_products:
            product_name = (product.find_element(By.CSS_SELECTOR, "div.card div.card-body h4").text).lower()
            log.info(product_name)
            if name in product_name:
                product.find_element(By.CSS_SELECTOR, "div.card div.card-footer button").click()
                log.info("product added")
                break
        log.info(self.driver.find_element(By.CSS_SELECTOR, "div#navbarResponsive a").text)
        print(self.driver.find_element(By.CSS_SELECTOR, "div#navbarResponsive a").text)
        self.driver.find_element(By.CSS_SELECTOR, "div#navbarResponsive a").click()
        self.driver.find_element(By.XPATH, "//tbody/tr[position()=last()]/td[5]").click()
        self.driver.find_element(By.ID, "country").send_keys("In")
        log.info("Entered the country name IND")

        # wait = WebDriverWait(self.driver, 10)
        # wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".suggestions")))
        #explicit wait
        self.wait_until_element_presence((By.CSS_SELECTOR, ".suggestions"))
        # time.sleep(10)
        countries = self.driver.find_elements(By.CSS_SELECTOR, "div.suggestions a")

        for country in countries:
            if country.text == "India":
                country.click()
                log.info("Choosen the India country from dynamic dropdown")
                break

        self.driver.find_element(By.CSS_SELECTOR, "div.checkbox.checkbox-primary").click()
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        message = self.driver.find_element(By.CSS_SELECTOR, "div.alert-success").text
        log.info(message)
        assert 1==2
        time.sleep(3)





