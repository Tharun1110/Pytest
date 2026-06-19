import pytest
from pages.postion_page import PostionPage
def test_postion(page, screenshot_dir, base_url, test_username, test_password):
    test_page = PostionPage(page, screenshot_dir)
    test_page.navigate(base_url)
    test_page.fill_email(test_username)
    test_page.fill_password(test_password)
    test_page.click_login()
    test_page.click_positions_link()
    test_page.fill_global_search("software Trainee")
    test_page.click_positions_button()