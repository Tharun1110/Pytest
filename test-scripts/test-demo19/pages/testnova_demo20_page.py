from playwright.sync_api import Page

class TestnovaDemo20Page:
    def __init__(self, page: Page, screenshot_dir: str):
        self.page = page
        self.screenshot_dir = screenshot_dir
         


        # Locators
        self.email_input = page.get_by_label('Email address')
        self.password_input = page.get_by_role('textbox', name='Password')
        self.login_form = page.locator('form')
        self.login_button = self.login_form.get_by_role('button')
        self.sidebar_link = page.locator('nav.sidebar-nav:nth-child(2) > ul.nav.flex-column:nth-child(1) > li.nav-item:nth-child(4) > a.nav-link:nth-of-type(1)')
        self.global_search_input = page.locator('#globalSearch')

    def _screenshot(self, name: str):
        self.page.screenshot(path=f'{self.screenshot_dir}/{name}')

    def navigate_to_login(self, base_url: str):
        self.page.goto(f'{base_url}/login/?next=/')
        self._screenshot('screenshot-1.png')

    def enter_email(self, email: str):
        self.email_input.fill(email)
        self._screenshot('screenshot-2.png')

    def press_tab_on_email(self):
        self.email_input.press('Tab')
        self._screenshot('screenshot-3.png')

    def enter_password(self, password: str):
        self.password_input.fill(password)
        self._screenshot('screenshot-4.png')

    def click_login(self):
        self.login_button.click()
        self._screenshot('screenshot-5.png')

    def click_sidebar_link(self):
        self.sidebar_link.click()
        self._screenshot('screenshot-6.png')

    def search_global(self, query: str):
        self.global_search_input.fill(query)
        self._screenshot('screenshot-7.png')

    def click_search_button(self):
        search_form = self.page.locator('form')
        search_button = search_form.get_by_role('button')
        search_button.click()
        self._screenshot('screenshot-8.png')