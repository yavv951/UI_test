from locators.login import BasePageLocators


class LoginPage:
    def __init__(self, app):
        self.app = app

    def auth(self, login: str, password: str):
        sign_in = self.app.driver.find_element(*BasePageLocators.SIGN_IN)
        sign_in.click()
        email_input = self.app.driver.find_element(*BasePageLocators.USER_NAME)
        email_input.send_keys(login)
        pass_input = self.app.driver.find_element(*BasePageLocators.PASSWORD)
        pass_input.send_keys(password)
        checkbox = self.app.driver.find_element(*BasePageLocators.SAVE_ME)
        checkbox.click()
        click_button = self.app.driver.find_element(*BasePageLocators.BUTTON)
        click_button.click()
