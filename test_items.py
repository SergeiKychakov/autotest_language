import pytest
from selenium import webdriver
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_button_on_page(browser):
        browser.get(link)
        time.sleep(5)
        assert browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
