import pytest
from pages.testcase_login_page import TestcaseLoginPage

def test_testcase_login(page, screenshot_dir, base_url, test_username, test_password):
    test_page = TestcaseLoginPage(page, screenshot_dir)
    test_page.navigate(base_url)
    test_page.fill_email(test_username)
    test_page.fill_password(test_password)
    test_page.click_login()
    test_page.verify_user_dropdown_contains(test_username)