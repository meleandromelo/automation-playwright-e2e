from playwright.sync_api import Page


class SortableTablePage:
    def __init__(self, page: Page):
        self.page = page
        table = page.locator("#table2")
        self.rows = table.locator("tbody tr")
        self.balances = table.locator("tbody td.dues")
        self.due_header = table.get_by_role("columnheader", name="Due")

    def open(self):
        self.page.goto("/tables")
