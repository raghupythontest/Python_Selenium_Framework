from selenium.webdriver.common.by import By


class HomePage:
    shop = (By.LINK_TEXT, "Shop")
    name = (By.XPATH, "//input[@name='name']")
    email = (By.NAME, "email")
    password = (By.CSS_SELECTOR, "#exampleInputPassword1")
    cBox = (By.ID, "exampleCheck1")
    submit = (By.XPATH, "//input[@type='submit']")
    dropdown = (By.ID, "exampleFormControlSelect1")
    alert_message=(By.CSS_SELECTOR, "div.alert-success")

    def __init__(self, driver):
        self.driver = driver

    def shop_nav(self):
        return self.driver.find_element(*HomePage.shop)

    def get_name_element(self):
        return self.driver.find_element(*HomePage.name)

    def get_email_element(self):
        return self.driver.find_element(*HomePage.email)

    def get_password_element(self):
        return self.driver.find_element(*HomePage.password)

    def get_checkBox(self):
        return self.driver.find_element(*HomePage.cBox)

    def get_dropdown(self):
        return self.driver.find_element(*HomePage.dropdown)

    def get_submitButton(self):
        return self.driver.find_element(*HomePage.submit)

    def getAlertMessage(self):
        return self.driver.find_element(*HomePage.alert_message)
