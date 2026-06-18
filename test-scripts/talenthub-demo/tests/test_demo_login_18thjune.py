import pytest
from pages.demo_login_18thjune_page import DemoLogin18thjunePage

def test_demo_login_18thjune(page, screenshot_dir, base_url, test_username, test_password):
    demo_page = DemoLogin18thjunePage(page, screenshot_dir)
    demo_page.navigate_to_login(base_url)
    demo_page.enter_email(test_username)
    demo_page.enter_password(test_password)
    demo_page.click_login()
    demo_page.verify_user_dropdown_contains(test_username)