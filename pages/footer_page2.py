from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import time


class Footer:
    def __init__(self, driver):
        """Класс для тестирования футера на сайте"""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Локаторы для основных разделов футера
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
        sleep(2)  # Увеличиваем время для стабильности

    def find_clickable_element(self, locator):
        """Находит кликабельный элемент с диагностикой"""
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            print(f"✅ Элемент найден и кликабелен")
            return element
        except Exception as e:
            print(f"❌ Элемент не кликабелен: {e}")
            # Пробуем найти элемент хотя бы присутствующим
            try:
                element = self.wait.until(EC.presence_of_element_located(locator))
                print(f"ℹ️ Элемент присутствует: {element.text}")
                return element
            except Exception as e2:
                print(f"❌ Элемент не найден: {e2}")
                raise
    
    def close_popup_if_exists(self):
        """Закрывает всплывающее окно если оно есть"""
        try:
            popup_close = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(self.close_locator)
            )
            popup_close.click()
            print("✅ Всплывающее окно закрыто")
            sleep(1)
        except:
            print("ℹ️ Всплывающего окна нет или оно уже закрыто")
    
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
        """Кликает на пункт меню с улучшенной обработкой"""
        print(f"🔄 Начинаем клик на '{item_name}'...")
        
        # Закрываем попап
        self.close_popup_if_exists()
        
        # Сохраняем текущий URL
        current_url = self.driver.current_url
        print(f"Текущий URL: {current_url}")
        
        # Скроллим к футеру
        self.scroll_to_footer()
        
        # Находим элемент
        element = self.find_clickable_element(locator)
        print(f"Найден элемент с текстом: '{element.text}'")
        
        # Дополнительная прокрутка к конкретному элементу
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        sleep(1)
        
        # Пробуем разные способы клика
        try:
            print("Пробуем обычный клик...")
            element.click()
            print("✅ Обычный клик выполнен")
        except Exception as e:
            print(f"❌ Обычный клик не сработал: {e}")
            try:
                print("Пробуем клик через JavaScript...")
                self.driver.execute_script("arguments[0].click();", element)
                print("✅ JavaScript клик выполнен")
            except Exception as e2:
                print(f"❌ JavaScript клик не сработал: {e2}")
                # Последняя попытка - через ActionChains
                try:
                    from selenium.webdriver.common.action_chains import ActionChains
                    print("Пробуем клик через ActionChains...")
                    actions = ActionChains(self.driver)
                    actions.move_to_element(element).click().perform()
                    print("✅ ActionChains клик выполнен")
                except Exception as e3:
                    print(f"❌ Все способы клика не сработали: {e3}")
                    raise
        
        print(f"✅ Клик на '{item_name}' выполнен")
        
        # Ждем загрузки новой страницы
        try:
            self.wait.until(EC.url_changes(current_url))
            new_url = self.driver.current_url
            print(f"✅ URL изменился: {new_url}")
        except Exception as e:
            print(f"⚠️ URL не изменился после клика: {e}")
            print(f"Текущий URL: {self.driver.current_url}")