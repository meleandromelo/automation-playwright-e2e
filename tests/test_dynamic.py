from playwright.sync_api import Page, expect

from pages.dynamic import DynamicControlsPage, DynamicLoadingPage


def test_result_rendered_after_start(page: Page):
    loading = DynamicLoadingPage(page)
    loading.open()
    expect(loading.result).to_have_count(0)
    loading.start.click()
    expect(loading.result).to_be_visible(timeout=15_000)


def test_asynchronous_form_controls(page: Page):
    form = DynamicControlsPage(page)
    form.open()

    expect(form.checkbox).to_be_visible()
    form.remove.click()
    expect(form.checkbox).to_have_count(0, timeout=15_000)
    form.add.click()
    expect(form.checkbox).to_be_visible(timeout=15_000)
    form.checkbox.check()
    expect(form.checkbox).to_be_checked()

    expect(form.textbox).to_be_disabled()
    form.enable.click()
    expect(form.textbox).to_be_enabled(timeout=15_000)
    form.textbox.fill("QA portfolio")
    form.disable.click()
    expect(form.textbox).to_be_disabled(timeout=15_000)
    expect(form.textbox).to_have_value("QA portfolio")
