from playwright.sync_api import Page


class DynamicLoadingPage:
    def __init__(self, page: Page):
        self.page = page
        self.start = page.get_by_role("button", name="Start")
        self.result = page.get_by_role("heading", name="Hello World!")

    def open(self):
        self.page.goto("/dynamic_loading/2")


class DynamicControlsPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkbox = page.get_by_role("checkbox")
        self.remove = page.get_by_role("button", name="Remove", exact=True)
        self.add = page.get_by_role("button", name="Add", exact=True)
        self.textbox = page.get_by_role("textbox")
        self.enable = page.get_by_role("button", name="Enable", exact=True)
        self.disable = page.get_by_role("button", name="Disable", exact=True)

    def open(self):
        self.page.goto("/dynamic_controls")
