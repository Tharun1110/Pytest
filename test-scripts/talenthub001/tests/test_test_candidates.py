import pytest
from pages.test_candidates_page import TestCandidatesPage

def test_test_candidates(page, screenshot_dir, base_url, test_username, test_password):
	test_page = TestCandidatesPage(page, screenshot_dir)
	test_page.navigate(base_url)
	test_page.fill_email(test_username)
	test_page.fill_password(test_password)
	test_page.click_login()
	test_page.click_third_link()
	test_page.fill_global_search("Tharun")
	test_page.click_search_button()