from pages.testnova_demo20_page import TestnovaDemo20Page

def test_testnova_demo20(page, screenshot_dir, base_url, test_username, test_password):
    test_page = TestnovaDemo20Page(page, screenshot_dir)
    test_page.navigate_to_login(base_url)
    test_page.enter_email(test_username)
    test_page.press_tab_on_email()
    test_page.enter_password(test_password)
    test_page.click_login()
    test_page.click_sidebar_link()
    test_page.search_global('Software ')
    test_page.click_search_button()