import pytest
from pages.testnova_demo19_page import TestnovaDemo19Page

def test_testnova_demo19(page, screenshot_dir, base_url, test_username, test_password):
    test_page = TestnovaDemo19Page(page, screenshot_dir)
    test_page.navigate_to_login(base_url)
    test_page.enter_email(test_username)
    test_page.enter_password(test_password)
    test_page.click_login()
    test_page.verify_user_dropdown_contains(test_username)