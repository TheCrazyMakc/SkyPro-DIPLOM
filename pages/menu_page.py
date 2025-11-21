from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MenuPage:
    def __init__(self, driver):
        """Класс для тестирования меню на сайте"""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Улучшенные локаторы для кнопок меню
        self.promotions_button_locator = (By.XPATH, "//a[contains(@href, 'promotions') or contains(., 'Акции')]")
        self.sales_button_locator = (By.XPATH, "//a[contains(@href, 'sale') or contains(., 'Распродажа')]")
        self.certificate_button_locator = (By.XPATH, "//a[contains(@href, 'certificate') or contains(., 'Сертификаты')]")
        self.bonusprogram_button_locator = (By.XPATH, "//a[contains(@href, 'bonus') or contains(., 'Программа лояльности')]")
        self.articles_button_locator = (By.XPATH, "//a[contains(@href, 'blog') or contains(., 'Блог')]")
        self.mainpage_button_locator = (By.CSS_SELECTOR, ".header-sticky__logo-link")
        
    def find_clickable_element(self, locator):
        """Находит кликабельный элемент"""
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    def click_promotions(self):
        """Кликает на кнопку 'Акции'"""
        self._click_menu_item(self.promotions_button_locator, "Акции")

    def click_sales(self):
        """Кликает на кнопку 'Распродажа'"""
        self._click_menu_item(self.sales_button_locator, "Распродажа")

    def click_certificate(self):
        """Кликает на кнопку 'Сертификаты'"""
        self._click_menu_item(self.certificate_button_locator, "Сертификаты")

    def click_bonusprogram(self):
        """Кликает на кнопку 'Программа лояльности'"""
        self._click_menu_item(self.bonusprogram_button_locator, "Программа лояльности")

    def click_articles(self):
        """Кликает на кнопку 'Блог'"""
        self._click_menu_item(self.articles_button_locator, "Блог")
    
    def _click_menu_item(self, locator, item_name):
        """Кликает на пункт меню"""
        element = self.find_clickable_element(locator)
        element.click()
        print(f"✅ Клик на '{item_name}' выполнен")
        # Ждем загрузки новой страницы
        self.wait.until(EC.url_changes(self.driver.current_url))