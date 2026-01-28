from core.HillelAuto.Forms.registration_form import RegistrationForm
import allure

@allure.epic("Authentication")
class Authentication:
    pass

@allure.feature("Registration form")
class TestRegistrationPositive(Authentication):
    @allure.story("Registration with valid user params")
    def test_positive_sign_up(self, home_page):
        registration_form = RegistrationForm(home_page).open_form()

        assert registration_form.is_registration_form_opened() is True, "Registration Form is opened"

        registration_form.do_registration()

        assert registration_form.is_registration_successful() == True, "Registration is Failed"

