from playwright.sync_api import Page


class CheckboxesPage:
    def __init__(self, page: Page):
        self.page = page
        # The demo presents two unlabeled checkboxes in a fixed order.
        boxes = page.get_by_role("checkbox")
        self.first = boxes.nth(0)
        self.second = boxes.nth(1)

    def open(self):
        self.page.goto("/checkboxes")


class DropdownPage:
    def __init__(self, page: Page):
        self.page = page
        self.menu = page.get_by_role("combobox")

    def open(self):
        self.page.goto("/dropdown")
