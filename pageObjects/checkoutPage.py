from selenium.webdriver.common.by import By


class CheckoutPage:
    all_products=(By.CSS_SELECTOR, "div.card")

    def __init__(self,driver):
        self.driver=driver


    def get_products(self):
        return self.driver.find_elements(*CheckoutPage.all_products)

