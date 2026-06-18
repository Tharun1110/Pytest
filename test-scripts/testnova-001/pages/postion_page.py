import os
from playwright.sync_api import Page

class PostionPage:
    def __init__(self, page: Page, screenshot_dir: str):
        self.page = page
        self.screenshot_dir = screenshot_dir
        self._screenshot_counter = 1

    def _screenshot(self):
        path = os.path.join(self.screenshot_dir, f"screenshot-{self._screenshot_counter}.png")
        self.page.screenshot(path=path)
        self._screenshot_counter += 1

    def navigate(self, base_url: str):
        self.page.goto(f"{base_url}/login/?next=/")
        self._screenshot()

    def fill_email(self, email: str):
        self.page.get_by_label("Email address").fill(email)
        self._screenshot()

    def fill_password(self, password: str):
        self.page.get_by_role("textbox", name="Password").fill(password)
        self._screenshot()

    def click_login(self):
        self.page.get_by_role("button").click()
        self._screenshot()

    def click_positions_link(self):
        self.page.locator("nav.sidebar-nav:nth-child(2) > ul.nav.flex-column:nth-child(1) > li.nav-item:nth-child(2) > a.nav-link:nth-of-type(1)").click()
        self._screenshot()

    def fill_global_search(self, query: str):
        self.page.locator("#globalSearch").fill(query)
        self._screenshot()

    def click_positions_button(self):
        self.page.locator("div", has_text="Positions All Status All").get_by_role("button").click()
        self._screenshot()