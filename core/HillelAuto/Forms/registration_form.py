import allure

from core.HillelAuto.Helpers.registration_helper import RegistrationHelper
from core.HillelAuto.Helpers.user import TestUser
from core.HillelAuto.Pages.home_page import HomePage
from playwright.sync_api import expect

class RegistrationForm:

    def __init__(self, home_page: HomePage):
        self.home_page = home_page
        self.page = home_page.page
        self.reg_helper = RegistrationHelper()
        self.user = TestUser()

    @allure.step("Open registration form")
    def open_form(self):
        self.page.locator(self.home_page.sign_up_button_locator).click()
        #self.page.wait_for_timeout(1000)
        return self

    @allure.step("Filing user name field")
    def fill_user_name(self, user_name):
        self.page.locator(self.reg_helper.user_name).fill(user_name)

    @allure.step("Filing user last name field")
    def fill_user_last_name(self, user_last_name):
        self.page.locator(self.reg_helper.user_last_name).fill(user_last_name)

    @allure.step("Filing user mail field")
    def fill_user_mail(self, user_mail):
        self.page.locator(self.reg_helper.user_mail).fill(user_mail)

    @allure.step("Filing user password field")
    def fill_user_password(self, user_password):
        self.page.locator(self.reg_helper.user_password).fill(user_password)

    @allure.step("Filing user password repeat field")
    def fill_user_password_repeat(self, user_password):
        self.page.locator(self.reg_helper.user_password_repeat).fill(user_password)

    def is_registration_form_opened(self) -> bool:
        try:
            expect(self.page.locator(self.reg_helper.registration_text_locator)).to_have_text('Registration')
            return True
        except AssertionError:
            return False

    def do_registration(self, user_name = None,
                        user_last_name = None,
                        user_mail = None,
                        user_password = None,
                        user_password_repeat = None):

        self.fill_registration_fields(user_name, user_last_name, user_mail, user_password, user_password_repeat)
        if self.page.locator(self.reg_helper.register_button).is_enabled():
            with allure.step("Click on enabled Register button"):
                self.page.locator(self.reg_helper.register_button).click()
        #self.page.wait_for_timeout(1000)
        return self

    def fill_registration_fields(self, user_name,
                                 user_last_name,
                                 user_mail,
                                 user_password,
                                 user_password_repeat):
        if user_name is None:
            u_name = self.user.name
            self.fill_user_name(u_name)
        else:
            self.fill_user_name(user_name)

        if user_last_name is None:
            u_last_name = self.user.last_name
            self.fill_user_last_name(u_last_name)
        else:
            self.fill_user_last_name(user_last_name)

        if user_mail is None:
            u_mail = self.user.mail
            self.fill_user_mail(u_mail)
        else:
            self.fill_user_mail(user_mail)

        if user_password_repeat is None and user_password is not None:
            self.fill_user_password(user_password)
            self.fill_user_password_repeat(user_password)
        if user_password_repeat is None and user_password is None:
            u_password = self.user.password
            self.fill_user_password(u_password)
            self.fill_user_password_repeat(u_password)

    def is_registration_successful(self):
        try:
            expect(self.page.locator(self.reg_helper.my_profile)).to_have_text('My profile')
            return True
        except AssertionError:
            return False


    def is_registration_failed_by_password_conditions(self):
        try:
            expect(self.page.get_by_text(self.reg_helper.error_password_text)).to_be_visible()
            return True
        except AssertionError:
            return False

    def is_registration_failed_by_name_length(self):
        try:
            expect(self.page.get_by_text(self.reg_helper.error_name_by_length)).to_be_visible()
            return True
        except AssertionError:
            return False

    def is_registration_failed_invalid_name(self):
        try:
            expect(self.page.get_by_text(self.reg_helper.error_name_invalid)).to_be_visible()
            return True
        except AssertionError:
            return False

    def is_registration_failed_invalid_name_and_length(self):
        try:
            expect(self.page.get_by_text(self.reg_helper.error_name_invalid) and self.page.get_by_text(self.reg_helper.error_name_by_length)).to_be_visible()
            return True
        except AssertionError:
            return False

    def is_registration_failed_incorrect_mail(self):
        try:
            expect(self.page.get_by_text(self.reg_helper.error_mail_text)).to_be_visible()
            return True
        except AssertionError:
            return False