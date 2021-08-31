from selenium.webdriver.remote.webelement import WebElement
from locators.login_page_locator import BasePageLocators, UserPageLocators
from models.auth import AuthData
from pages.base_page import BasePage


class LoginPage(BasePage):
    def is_auth(self):
        self.find_element(BasePageLocators.FORM)
        element = self.find_elements(BasePageLocators.USER_BUTTON)
        if len(element) > 0:
            return True
        return False

    # Переход на страницу авторизации.
    def go_on_login_page(self):
        sign_in = self.find_element(BasePageLocators.PYTHON_BUTTON)
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

    """def auth(self, data: AuthData):
        if self.is_auth():
            self.click_element(self.user_menu())
            self.click_element(self.exit())
        self.fill_element(self.email_input(), data.login)
        self.fill_element(self.password_input(), data.password)
        self.click_element(self.submit_button())"""

    def auth_login_error(self) -> str:
        return self.find_element(BasePageLocators.LOGIN_ERROR).text

    def auth(self, data: AuthData):
        if self.is_auth():
            self.click_element(self.user_menu())
            self.click_element(self.exit())
        if self.is_exit_confirm_button():
            self.click_element(self.exit_confirm()[0])
        self.fill_element(self.email_input(), data.login)
        self.fill_element(self.password_input(), data.password)
        self.click_element(self.submit_button())

    def is_exit_confirm_button(self):
        self.find_element(BasePageLocators.FORM)
        element = self.find_elements(BasePageLocators.EXIT_CONFIRM)
        if len(element) > 0:
            return True
        return False

    def exit_confirm(self):
        return self.find_elements(BasePageLocators.EXIT_CONFIRM)

    # ________________________________________________________________________________________________
    # locators for update user information

    def about_user(self):
        return self.find_element(BasePageLocators.MENU_ACTION)

    def about_user_2(self):
        return self.find_element(BasePageLocators.MENU_ACTION_2)

    def edit_profile(self):
        return self.find_element(UserPageLocators.EDIT_INFO)

    # Переход в редактированеи информации через кнопку "настройка"
    def update_user(self):
        self.click_element(self.user_menu())
        self.click_element(self.about_user())
        self.click_element(self.edit_profile())

    # Переход в редактированеи информации через кнопку "о пользователе"
    def update_user_2(self):
        self.click_element(self.user_menu())
        self.click_element(self.about_user_2())
        self.find_element(UserPageLocators.EDIT_INFO)

    def input_firstname(self):
        self.find_element(UserPageLocators.FIRST_NAME)

    def input_lastname(self):
        self.find_element(UserPageLocators.LAST_NAME)

    def input_email(self):
        self.find_element(UserPageLocators.EMAIL)

    def submit_button_prof(self):
        self.find_element(UserPageLocators.SUBMIT)

    def submit_changes(self):
        self.click_element(self.submit_button_prof())
