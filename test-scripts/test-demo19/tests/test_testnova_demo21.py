import pytest
from pages.testnova_demo21_page import TestnovaDemo21Page

def test_testnova_demo21(page, screenshot_dir, base_url, test_username, test_password):
    test_page = TestnovaDemo21Page(page, screenshot_dir)
    test_page.navigate_to_login(base_url)
    test_page.enter_email(test_username)
    test_page.enter_password(test_password)
    test_page.click_login()
    test_page.click_sidebar_link()
    test_page.search_global("software Trainee")
    test_page.click_positions_button()