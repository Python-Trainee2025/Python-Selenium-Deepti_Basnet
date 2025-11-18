from selenium.webdriver.common.by import By

class CartPage:
    REMOVE_BIKE = (By.ID, "remove-sauce-labs-bike-light")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")

    def __init__(self, driver):
        self.driver = driver

    def remove_bike_light(self):
        self.driver.find_element(*self.REMOVE_BIKE).click()

    def continue_shopping(self):
        self.driver.find_element(*self.CONTINUE_SHOPPING).click()
