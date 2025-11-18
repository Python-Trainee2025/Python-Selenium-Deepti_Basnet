from selenium.webdriver.common.by import By

class ItemPage:
    ADD_TO_CART = (By.ID, "add-to-cart")

    def __init__(self, driver):
        self.driver = driver

    def add_item(self):
        self.driver.find_element(*self.ADD_TO_CART).click()