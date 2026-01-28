from core.HillelAuto.Forms.login_form import LoginForm
from core.HillelAuto.Forms.registration_form import RegistrationForm

import allure

from core.HillelAuto.Pages.home_page import HomePage


@allure.epic("Home Page")
@allure.feature("Home page availability")
@allure.story("Home page opens successfully")
def test_open_home_page(pw_page):
    home_page = HomePage(pw_page).open_page()
    assert home_page.is_home_page_opened() is True, "Home Page is opened"

@allure.epic("Authentication")
@allure.feature("Registration form availability")
@allure.story("Registration form opens from home page")
def test_open_sign_up_form(home_page):
    registration_form = RegistrationForm(home_page).open_form()
    assert registration_form.is_registration_form_opened() is True, "Registration Form is opened"


@allure.epic("Authentication")
@allure.feature("Login form availability")
@allure.story("Login form opens from home page")
def test_open_sign_in_form(home_page):
    login_form = LoginForm(home_page).open_form()
    assert login_form.is_login_form_opened() is True, "Login Form is opened"