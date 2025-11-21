import pytest
from pages.main_page import MainPage
from pages.footer_page2 import Footer


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