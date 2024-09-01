class LoginLocators:
    username_input = 'user-name'
    password_input = 'password'
    login_button = 'login-button'
    username_error = "//div[@class='login-box']//div[1]//*[name()='svg']"
    password_error = "//div[@class='login_wrapper-inner']//div[2]//*[name()='svg']"
    alert_box_error = "//div[@class='error-message-container error']"
    alert_locked_msg = "//h3[@data-test='error']"
