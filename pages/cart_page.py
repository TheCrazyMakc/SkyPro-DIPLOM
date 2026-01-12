from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.cart_item_count_locator = (
            By.CSS_SELECTOR, ".cart-page__title--append")
        
    def get_cart_items_count(self):
        """Возвращает количество товаров в корзине"""
        return len(self.driver.find_elements(By.CSS_SELECTOR, "div.chg-app-button__content"))
