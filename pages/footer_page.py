from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Footer:
    def __init__(self, driver):
        """Класс для тестирования футера на сайте"""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Локаторы для основных разделов футера (в вашем стиле)
        self.discount_locator = (By.XPATH, "//a[contains(@class, 'app-footer__info-links-link') and text()='Акции']")
        self.sales_locator = (By.XPATH, "//a[contains(@class, 'app-footer__info-links-link') and text()='Распродажа']")
        self.delivery_locator = (By.XPATH, "//a[contains(@class, 'app-footer__info-links-link') and text()='Доставка и оплата']")
        self.programm_locator = (By.XPATH, "//a[contains(@class, 'app-footer__info-links-link') and text()='Программа лояльности']")
        self.gift_locator = (By.XPATH, "//a[contains(@class, 'app-footer__info-links-link') and text()='Подарочные сертификаты']")
        self.close_locator = (By.XPATH, "//div[contains(@class, 'popmechanic-close') and text()='×']")

    def scroll_to_footer(self):
        """Прокручивает страницу к футеру"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print("✅ Прокрутка к футеру выполнена")
        sleep(1)  # Даем время на прокрутку

    def find_clickable_element(self, locator):
        """Находит кликабельный элемент"""
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    def click_discount(self):
        """Кликает на кнопку 'Акции'"""
        self.click_menu_item(self.discount_locator, "Акции")

    def click_sales(self):
        """Кликает на кнопку 'Распродажа'"""
        self.click_menu_item(self.sales_locator, "Распродажа")

    def click_delivery(self):
        """Кликает на кнопку 'Доставка и оплата'"""
        self.click_menu_item(self.delivery_locator, "Доставка и оплата")

    def click_programm(self):
        """Кликает на кнопку 'Программа лояльности'"""
        self.click_menu_item(self.programm_locator, "Программа лояльности")

    def click_gift(self):
        """Кликает на кнопку 'Подарочные сертификаты'"""
        self.click_menu_item(self.gift_locator, "Подарочные сертификаты")
    
    def click_menu_item(self, locator, item_name):
        """Кликает на пункт меню"""
        self.scroll_to_footer()
        element = self.find_clickable_element(locator)
        element.click()
        print(f"✅ Клик на '{item_name}' выполнен")
        # Ждем загрузки новой страницы
        self.wait.until(EC.url_changes(self.driver.current_url))
        # try:
        #     element.click()
        # except Exception:
        #     # Если прямой клик не срабатывает, можно кликом через JS как запасной вариант
        #     self.driver.execute_script("arguments[0].click();", element)
        # print(f"✅ Клик на '{item_name}' выполнен")
        # self.wait.until(EC.url_changes(self.driver.current_url))