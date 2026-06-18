from playwright.sync_api import Page

class DemoCandidatesUsersPage:
    def __init__(self, page: Page, screenshot_dir: str):
        self.page = page
        self.screenshot_dir = screenshot_dir

    def navigate_to_login(self, base_url: str):
        url = f"{base_url}/login/?next=/"
        self.page.goto(url)
        self.page.screenshot(path=f"{self.screenshot_dir}/screenshot-1.png")

    def enter_email(self, email: str):
        self.page.get_by_label("Email address").fill(email)
        self.page.screenshot(path=f"{self.screenshot_dir}/screenshot-2.png")

    def enter_password(self, password: str):
        self.page.get_by_role("textbox", name="Password").fill(password)
        self.page.screenshot(path=f"{self.screenshot_dir}/screenshot-3.png")

    def click_login(self):
        self.page.locator("form").get_by_role("button").click()
        self.page.screenshot(path=f"{self.screenshot_dir}/screenshot-4.png")

    def click_third_link(self):
        self.page.get_by_role("link").nth(3).click()
        self.page.screenshot(path=f"{self.screenshot_dir}/screenshot-5.png")

    def search_global(self, query: str):
        self.page.locator("#globalSearch").fill(query)
        self.page.screenshot(path=f"{self.screenshot_dir}/screenshot-6.png")

    def click_search_button(self):
        self.page.locator("form").get_by_role("button").click()
        self.page.screenshot(path=f"{self.screenshot_dir}/screenshot-7.png")