import pytest
from pages.demo_candidates_users_page import DemoCandidatesUsersPage

def test_demo_candidates_users(page, screenshot_dir, base_url, test_username, test_password):
    demo_page = DemoCandidatesUsersPage(page, screenshot_dir)
    demo_page.navigate_to_login(base_url)
    demo_page.enter_email(test_username)
    demo_page.enter_password(test_password)
    demo_page.click_login()
    demo_page.click_third_link()
    demo_page.search_global("Tharun")
    demo_page.click_search_button()