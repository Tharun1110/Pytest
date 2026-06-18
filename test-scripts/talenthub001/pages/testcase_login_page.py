import os
from playwright.sync_api import Page, expect

class TestcaseLoginPage:
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

    def verify_user_dropdown_contains(self, email: str):
        expect(self.page.locator("#userDropdown")).to_contain_text(email)
        self._screenshot()