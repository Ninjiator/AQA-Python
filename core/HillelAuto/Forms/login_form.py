import allure
from playwright.sync_api import expect
from core.HillelAuto.Pages.home_page import HomePage
from utils.settings import d_settings


class LoginForm:
    sign_in_button_locator = "role=button[name='Sign In']"
    login_text_locator = ".modal-title"
    sign_in_mail_field_locator = "#signinEmail"
    sign_in_password_field_locator = "#signinPassword"
    my_profile_button_locator = "button.user-nav_toggle"
    login_button = "role=button[name='Login']"

    def __init__(self, home_page : HomePage):
        self.home_page = home_page
        self.page = self.home_page.page

    @allure.step("Open Login form")
    def open_form(self):
        self.page.locator(self.sign_in_button_locator).click()
        #self.page.wait_for_timeout(1000)
        return self


    def do_login(self):
        with allure.step("Fill USER_MAIL from secrets"):
            self.page.locator(self.sign_in_mail_field_locator).fill(d_settings.USER_MAIL)

        with allure.step("Fill USER_PASS from secrets"):
            self.page.locator(self.sign_in_password_field_locator).fill(d_settings.USER_PASS)

        with allure.step("Click on login button"):
            self.page.locator(self.login_button).click()

        return self

    def is_login_success(self):
        try:
            expect(self.page.locator(self.my_profile_button_locator)).to_have_text('My profile', timeout=1000)
            return True
        except AssertionError:
            return False

    def is_login_form_opened(self):
        try:
            expect(self.page.locator(self.login_text_locator)).to_have_text('Log in', timeout=1000)
            return True
        except AssertionError:
            return False