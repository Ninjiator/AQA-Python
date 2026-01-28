

class RegistrationHelper:

    registration_text_locator = ".modal-title"

    user_name = "#signupName"
    user_last_name = "#signupLastName"
    user_mail = "#signupEmail"
    user_password = "#signupPassword"
    user_password_repeat = "#signupRepeatPassword"
    register_button = "role=button[name='Register']"
    my_profile = "button.user-nav_toggle"

    error_name_by_length = "Name has to be from 2 to 20 characters long"
    error_name_invalid = "Name is invalid"
    error_last_name = "Last name has to be from 2 to 20 characters long"
    error_mail_text = "Email is incorrect"
    error_password_text = "Password has to be from 8 to 15 characters long and contain at least one integer, one capital, and one small letter"
