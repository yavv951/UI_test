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

    # Переход на страницу авторизации.
    def go_on_login_page(self):
        sign_in = self.app.driver.find_element(*BasePageLocators.PYTHON_BUTTON)
        sign_in.click()
    # Функция указывает на то,что мы находимся или нет на странице авторизации.
    def login_page_y(self):
        element = self.find_elements(BasePageLocators.TEXT_LOGIN_PAGE)
        if len(element) > 0:
            return True
        return False

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


    def auth(self, data: AuthData):
        if self.is_auth():
            self.click_element(self.user_menu())
            self.click_element(self.exit())
        self.fill_element(self.email_input(), data.login)
        self.fill_element(self.password_input(), data.password)
        self.click_element(self.submit_button())

    def auth_login_error(self) -> str:
        return self.find_element(BasePageLocators.LOGIN_ERROR).text