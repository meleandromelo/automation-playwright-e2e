import re

import pytest
from playwright.sync_api import Page, expect

from data.demo import DEMO_PASSWORD, DEMO_USER
from pages.authentication import AuthenticationPage


def test_login_and_logout(page: Page):
    form = AuthenticationPage(page)
    form.open()
    form.login(DEMO_USER, DEMO_PASSWORD)

    expect(page).to_have_url(re.compile(r"/secure$"))
    expect(form.notice).to_contain_text("You logged into a secure area!")
    form.logout.click()
    expect(page).to_have_url(re.compile(r"/login$"))
    expect(form.notice).to_contain_text("You logged out of the secure area!")


@pytest.mark.parametrize(
    ("username", "password", "message"),
    [
        pytest.param("unknown-qa-user", DEMO_PASSWORD, "Your username is invalid!", id="invalid-user"),
        pytest.param(DEMO_USER, "wrong-password", "Your password is invalid!", id="invalid-password"),
    ],
)
def test_rejected_credentials(page: Page, username: str, password: str, message: str):
    form = AuthenticationPage(page)
    form.open()
    form.login(username, password)

    expect(form.notice).to_contain_text(message)
    expect(page).to_have_url(re.compile(r"/login$"))
    expect(form.login_button).to_be_visible()
