import pytest
from pages.main_page import MainPage
from pages.search_page import SearchPage
from pages.cart_page import CartPage
from pages.menu_page import MenuPage
from pages.footer_page import Footer
from data import SEARCH_FOR_CART_PHRASES
from data import SEARCH_PHRASES
from time import sleep
import allure


@allure.title("Тест поиска книг. POSITIVE")
@allure.description("Этот тест проверяет, что поиск книг работает корректно.")
@allure.feature("READ")
@allure.severity("CRITICAL")
@pytest.mark.parametrize("search_query", SEARCH_PHRASES)
@pytest.mark.search
def test_search_main(browser, search_query):
    page = MainPage(browser)
    page.open()
    page.search(search_query)

    search_page = SearchPage(browser)
    search_page.wait_for_search_results()
    results_count = search_page.get_results_count()

    assert results_count > 0



@allure.title("Тест добавления книг в корзину. POSITIVE")
@allure.description("Этот тест проверяет, что поиск книги добавляются в корзину.")
@allure.feature("READ")
@allure.severity("CRITICAL")
@pytest.mark.parametrize("search_query", SEARCH_FOR_CART_PHRASES)
@pytest.mark.cart
def test_add_to_cart_flow(browser, search_query):
    """Тест поиску и добавлению товара в корзину"""
    main_page = MainPage(browser)
    main_page.open()
    main_page.search(search_query)

    search_page = SearchPage(browser)
    search_page.wait_for_search_results()
    search_page.add_first_product_to_cart()
    search_page.go_to_cart()

    cart_page = CartPage(browser)
    sleep(3)
    assert cart_page.get_cart_items_count()



@allure.title("Тест проверки меню. POSITIVE")
@allure.description("Этот тест проверяет, что осуществляется переход по кнопкам в меню.")
@allure.feature("READ")
@allure.severity("CRITICAL")
@pytest.mark.menu
def test_promotions_menu(browser):
    """Тест перехода в раздел Акции"""
    main_page = MainPage(browser)
    main_page.open()
    
    menu_page = MenuPage(browser)
    menu_page.click_promotions()


@pytest.mark.menu  
def test_sales_menu(browser):
    """Тест перехода в раздел Распродажа"""
    main_page = MainPage(browser)
    main_page.open()
    
    menu_page = MenuPage(browser)
    menu_page.click_sales()


@pytest.mark.menu
def test_certificate_menu(browser):
    """Тест перехода в раздел Сертификаты"""
    main_page = MainPage(browser)
    main_page.open()
    
    menu_page = MenuPage(browser)
    menu_page.click_certificate()


@pytest.mark.menu
def test_bonusprogram_menu(browser):
    """Тест перехода в раздел Программа лояльности"""
    main_page = MainPage(browser)
    main_page.open()
    
    menu_page = MenuPage(browser)
    menu_page.click_bonusprogram()


@pytest.mark.menu
def test_articles_menu(browser):
    """Тест перехода в раздел Блог"""
    main_page = MainPage(browser)
    main_page.open()
    
    menu_page = MenuPage(browser)
    menu_page.click_articles()




@allure.title("Тест проверки футера. POSITIVE")
@allure.description("Этот тест проверяет, что осуществляется переход по кнопкам в футер меню.")
@allure.feature("READ")
@allure.severity("CRITICAL")
@pytest.mark.footer
def test_discount_footer(browser):
    """Тест перехода в раздел 'Акции' из футера"""
    main_page = MainPage(browser)
    main_page.open()
    
    footer_page = Footer(browser)
    footer_page.click_discount()


@pytest.mark.footer
def test_sales_footer(browser):
    """Тест перехода в раздел 'Распродажа' из футера"""
    main_page = MainPage(browser)
    main_page.open()
    
    footer_page = Footer(browser)
    footer_page.click_sales()


@pytest.mark.footer
def test_delivery_footer(browser):
    """Тест перехода в раздел 'Доставка и оплата' из футера"""
    main_page = MainPage(browser)
    main_page.open()
    
    footer_page = Footer(browser)
    footer_page.click_delivery()


@pytest.mark.footer
def test_programm_footer(browser):
    """Тест перехода в раздел 'Программа лояльности' из футера"""
    main_page = MainPage(browser)
    main_page.open()
    
    footer_page = Footer(browser)
    footer_page.click_programm()


@pytest.mark.footer
def test_gift_footer(browser):
    """Тест перехода в раздел 'Подарочные сертификаты' из футера"""
    main_page = MainPage(browser)
    main_page.open()
    
    footer_page = Footer(browser)
    footer_page.click_gift()