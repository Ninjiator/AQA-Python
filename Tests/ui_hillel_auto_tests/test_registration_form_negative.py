from core.HillelAuto.Forms.registration_form import RegistrationForm
import pytest
import allure
from Tests.ui_hillel_auto_tests.test_registration_form_positive import Authentication


@allure.feature("Registration form")
class TestRegistrationNegative(Authentication):

    @allure.story("Registration with invalid user password")
    @pytest.mark.parametrize("password", [
        ("aaa"),
        ("SEGEDSPDF"),
        ("abcdefgh!"),
        ("abcdefgh!aiosdfmg[iopasmdf[pgioms][pdfjmg]p[oim"),
        ("1247312843"),
    ])
    def test_negative_sign_up_password(self, home_page, password):
        registration_form = RegistrationForm(home_page).open_form().do_registration(user_password=password)
        assert registration_form.is_registration_failed_by_password_conditions() == True, "Registration is failed due to password error"

    @allure.story("Registration with a to long/short username")
    @pytest.mark.parametrize("name", [
        ("a"),
        ("MarkMichelJaksonJamisonDerrelLilianDanielHenderson")])

    def test_negative_sign_up_name_length(self, home_page, name):
        registration_form = RegistrationForm(home_page).open_form().do_registration(user_name=name)
        assert registration_form.is_registration_failed_by_name_length() == True, "Registration is failed due to name length"

    @allure.story("Registration with a symbols, numbers in username")
    @pytest.mark.parametrize("name", [
        ("Mark2"),
        ("1"),
        ("!@$@$"),
    ])
    def test_negative_sign_up_name_invalid(self, home_page, name):
        registration_form = RegistrationForm(home_page).open_form().do_registration(user_name=name)
        assert registration_form.is_registration_failed_invalid_name() == True, "Registration is failed due to invalid name"

    @pytest.mark.parametrize("name", [
        ("Mark_Michel_Jakson_Jamison_Derrel_2010"),
        ("@"),
    ])
    @allure.story("Registration with use of symbols, numbers where username is to long or to short ")
    def test_negative_sign_up_invalid_name_and_length(self, home_page, name):
        registration_form = RegistrationForm(home_page).open_form().do_registration(user_name=name)
        assert registration_form.is_registration_failed_invalid_name_and_length() == True, "Registration is failed due to invalid name and name length"

    @allure.story("Registration with invalid structure of user email")
    @pytest.mark.parametrize("mail", [
        ("test@gmail."),
        ("myPost.post"),
    ])
    def test_negative_sign_up_mail(self, home_page, mail):
        registration_form = RegistrationForm(home_page).open_form().do_registration(user_mail=mail)
        assert registration_form.is_registration_failed_incorrect_mail() == True, "Registration is failed due to incorrect email"



