import pytest
from pages.main_page import MainPage
from pages.menu_page import MenuPage


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