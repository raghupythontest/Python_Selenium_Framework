import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
def test_chromeDevTool():
    service_obj=Service("C:/Development/chromedriver")
    driver=webdriver.Chrome(service=service_obj)
    driver.get("https://super.walmart.com.mx/")
    driver.maximize_window()

    driver.refresh()

    time.sleep(3)
    # driver.close()