import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()

login_data = [
    ("standard_user","secret_sauce"),
     ("problem_user","secret_sauce"),
     ("performance_glitch_user","secret_sauce")
]


for username, password in login_data:
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    driver.get("https://saucedemo.com/")


    driver.find_element(By.ID,"user-name").send_keys(username)
    driver.find_element(By.ID,"password").send_keys(password)
    driver.find_element(By.ID,"login-button").click()
    time.sleep(2)


    driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(1)

    # cart_items=driver.find_element(By.CLASS_NAME, "shopping_cart_item")
    # time.sleep(1)


    driver.find_element(By.ID, "remove-sauce-labs-bike-light").click()
    time.sleep(1)

    driver.find_element(By.ID, "continue-shopping").click()
    time.sleep(5)
    driver.find_element(By.LINK_TEXT, "Sauce Labs Fleece Jacket").click()
    time.sleep(1)
    driver.find_element(By.ID, "add-to-cart").click()
    time.sleep(1)
    driver.quit()


