import time

from selenium.webdriver.common.by import By


def test_page_has_button_add_to_basket(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    assert bool(browser.find_elements(By.CLASS_NAME, 'btn-add-to-basket')) is True, 'Can`n find "Add to basket" button'
