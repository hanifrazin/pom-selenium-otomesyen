from selenium.webdriver.common.by import By
from locators.login_locators import LoginLocators


class LoginPages:
    def __init__(self, driver):
        self.driver = driver

    def input_username(self, username):
        self.driver.find_element(By.ID, LoginLocators.username_input).send_keys(username)

    def error_username(self):
        return self.driver.find_element(By.XPATH, LoginLocators.username_error).is_displayed()

    def input_password(self, password):
        self.driver.find_element(By.ID, LoginLocators.password_input).send_keys(password)

    def error_password(self):
        return self.driver.find_element(By.XPATH, LoginLocators.password_error).is_displayed()

    def click_login_button(self):
        self.driver.find_element(By.ID, LoginLocators.login_button).click()

    def error_box(self):
        return self.driver.find_element(By.XPATH, LoginLocators.alert_box_error).is_displayed()

    def error_msg(self):
        return self.driver.find_element(By.XPATH, LoginLocators.alert_locked_msg).text

    def clear_field(self):
        self.driver.find_element(By.ID, LoginLocators.username_input).clear()
        self.driver.find_element(By.ID, LoginLocators.password_input).clear()
