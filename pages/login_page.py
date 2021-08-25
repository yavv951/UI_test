from selenium.webdriver.remote.webelement import WebElement

from UI_test.locators.login_page_locator import BasePageLocators
from UI_test.models.auth import AuthData
from UI_test.pages.base_page import BasePage


class LoginPage(BasePage):
    def is_auth(self):
        self.find_element(BasePageLocators.FORM)
        element = self.find_elements(BasePageLocators.USER_BUTTON)
        if len(element) > 0:
            return True
        return False

    """def auth(self, login: str, password: str):
        sign_in = self.app.driver.find_element(*BasePageLocators.SIGN_IN)
        sign_in.click()
        email_input = self.app.driver.find_element(*BasePageLocators.USER_NAME)
        email_input.send_keys(login)
        pass_input = self.app.driver.find_element(*BasePageLocators.PASSWORD)
        pass_input.send_keys(password)
        checkbox = self.app.driver.find_element(*BasePageLocators.SAVE_ME)
        checkbox.click()
        click_button = self.app.driver.find_element(*BasePageLocators.BUTTON)
        click_button.click()"""

    def email_input(self) -> WebElement:
        return self.find_element(BasePageLocators.LOGIN)

    def password_input(self) -> WebElement:
        return self.find_element(BasePageLocators.PASSWORD)

    def submit_button(self) -> WebElement:
        return self.find_element(BasePageLocators.SUBMIT)

    def user_menu(self) -> WebElement:
        return self.find_element(BasePageLocators.USER_MENU)

    def exit(self) -> WebElement:
        return self.find_element(BasePageLocators.EXIT)

    #def sing_in(self):
        #return self.find_element()

    def auth(self, data: AuthData):
        if self.is_auth():
            self.click_element(self.user_menu())
            self.click_element(self.exit())
        self.fill_element(self.email_input(), data.login)
        self.fill_element(self.password_input(), data.password)
        self.click_element(self.submit_button())

    def auth_login_error(self) -> str:
        return self.find_element(BasePageLocators.LOGIN_ERROR).text