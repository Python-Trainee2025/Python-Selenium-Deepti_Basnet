import time
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.item_page import ItemPage

login_data = [
    ("standard_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce")
]

@pytest.mark.parametrize("username,password", login_data)
def test_saucedemo_flow(driver, username, password):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    item = ItemPage(driver)

    login.open()
    login.login(username, password)
    time.sleep(2)

    inventory.add_backpack()
    inventory.add_bike_light()
    inventory.open_cart()
    time.sleep(1)

    cart.remove_bike_light()
    time.sleep(1)

    cart.continue_shopping()
    time.sleep(2)

    inventory.open_fleece_jacket()
    time.sleep(1)

    item.add_item()
    time.sleep(1)
