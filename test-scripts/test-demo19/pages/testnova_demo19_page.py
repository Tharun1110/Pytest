from playwright.sync_api import Page, expect

class TestnovaDemo19Page:
    def __init__(self, page: Page, screenshot_dir: str):
        self.page = page
        self.screenshot_dir = screenshot_dir

        # Locators
        self.email_input = page.get_by_label('Email address')
        self.password_input = page.get_by_role('textbox', name='Password')
        self.login_form = page.locator('form')
        self.login_button = self.login_form.get_by_role('button')
        self.user_dropdown = page.locator('#userDropdown')

    def _screenshot(self, name: str):
        self.page.screenshot(path=f'{self.screenshot_dir}/{name}')

    def navigate_to_login(self, base_url: str):
        self.page.goto(f'{base_url}/login/?next=/')
        self._screenshot('screenshot-1.png')

    def enter_email(self, email: str):
        self.email_input.fill(email)
        self._screenshot('screenshot-2.png')

    def enter_password(self, password: str):
        self.password_input.fill(password)
        self._screenshot('screenshot-3.png')

    def click_login(self):
        self.login_button.click()
        self._screenshot('screenshot-4.png')

    def verify_user_dropdown_contains(self, email: str):
        expect(self.user_dropdown).to_contain_text(email)
        self._screenshot('screenshot-5.png')