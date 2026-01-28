from core.HillelAuto.Forms.login_form import LoginForm
import allure
from Tests.ui_hillel_auto_tests.test_registration_form_positive import Authentication



@allure.feature("Login form")
class TestLoginForm(Authentication):

    @allure.story("Login of existing user")
    def test_positive_sign_in(self, home_page):
        login_form = LoginForm(home_page).open_form()
        assert login_form.is_login_form_opened() is True, "Login Form is opened"
        login_form.do_login()
        assert login_form.is_login_success() == True, "Login is failed"