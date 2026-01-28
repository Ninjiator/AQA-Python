import allure

from core.HillelAuto.Forms.login_form import LoginForm

from playwright.sync_api import sync_playwright
import pytest

from core.HillelAuto.Pages.home_page import HomePage


@pytest.fixture(scope='session')
def pw_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        yield page

@pytest.fixture()
def home_page(brand_new_page):
    home_page = HomePage(brand_new_page)
    with allure.step("Open Home Page"):
        home_page.open_page()
    return home_page

@pytest.fixture()
def brand_new_page(pw_page):
    browser = pw_page.context.browser
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture(scope="session")
def authorized_page(home_page):
    login_form = LoginForm(home_page).open_form().do_login()
    return login_form