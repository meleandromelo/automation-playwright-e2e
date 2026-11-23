from decimal import Decimal

from playwright.sync_api import Page, expect

from pages.alerts import AlertsPage
from pages.inputs import CheckboxesPage, DropdownPage
from pages.tables import SortableTablePage


def test_checkbox_and_dropdown_selections(page: Page):
    boxes = CheckboxesPage(page)
    boxes.open()
    expect(boxes.first).not_to_be_checked()
    expect(boxes.second).to_be_checked()
    boxes.first.check()
    boxes.second.uncheck()
    expect(boxes.first).to_be_checked()
    expect(boxes.second).not_to_be_checked()

    dropdown = DropdownPage(page)
    dropdown.open()
    for value in ("2", "1"):
        dropdown.menu.select_option(label=f"Option {value}")
        expect(dropdown.menu).to_have_value(value)


def test_javascript_dialog_responses(page: Page):
    alerts = AlertsPage(page)
    alerts.open()

    assert alerts.respond("Click for JS Alert", accept=True) == ("alert", "I am a JS Alert")
    expect(alerts.result).to_have_text("You successfully clicked an alert")
    assert alerts.respond("Click for JS Confirm", accept=False) == ("confirm", "I am a JS Confirm")
    expect(alerts.result).to_have_text("You clicked: Cancel")
    assert alerts.respond("Click for JS Prompt", accept=True, answer="QA") == ("prompt", "I am a JS prompt")
    expect(alerts.result).to_have_text("You entered: QA")


def test_sort_balances_in_both_directions(page: Page):
    table = SortableTablePage(page)
    table.open()
    expect(table.balances.first).to_be_visible()
    original_rows = sorted(table.rows.all_inner_texts())
    amounts = table.balances.all_text_contents()
    assert len(set(amounts)) > 1
    ascending = sorted(amounts, key=lambda amount: Decimal(amount.strip().removeprefix("$")))

    table.due_header.click()
    expect(table.balances).to_have_text(ascending)
    assert sorted(table.rows.all_inner_texts()) == original_rows
    table.due_header.click()
    expect(table.balances).to_have_text(list(reversed(ascending)))
    assert sorted(table.rows.all_inner_texts()) == original_rows
