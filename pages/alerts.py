from playwright.sync_api import Dialog, Page


class AlertsPage:
    def __init__(self, page: Page):
        self.page = page
        self.result = page.locator("#result")

    def open(self):
        self.page.goto("/javascript_alerts")

    def respond(self, button: str, *, accept: bool, answer: str | None = None) -> tuple[str, str]:
        observed = []

        def handle(dialog: Dialog):
            observed.append((dialog.type, dialog.message))
            if accept:
                dialog.accept(prompt_text=answer)
            else:
                dialog.dismiss()

        self.page.once("dialog", handle)
        self.page.get_by_role("button", name=button, exact=True).click()
        return observed[0]
