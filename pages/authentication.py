from playwright.sync_api import Page


class AuthenticationPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.get_by_label("Username")
        self.password = page.get_by_label("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.notice = page.locator("#flash")
        self.logout = page.get_by_role("link", name="Logout")

    def open(self):
        self.page.goto("/login")

    def login(self, username: str, password: str):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
