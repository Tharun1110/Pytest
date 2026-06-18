from playwright.sync_api import Page, expect

class DemoLogin18thjunePage:
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

    def verify_user_dropdown_contains(self, email: str):
        expect(self.page.locator("#userDropdown")).to_contain_text(email)
        self.page.screenshot(path=f"{self.screenshot_dir}/screenshot-5.png")