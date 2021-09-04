import time
from selenium.webdriver.remote.webelement import WebElement
import logging
from UI_test.locators.login_page_locator import BasePageLocators, UserPageLocators
from UI_test.models.auth import AuthData, PersonalData
from UI_test.pages.base_page import BasePage

logger = logging.getLogger("moodle")


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
        logger.info(f'User email is "{data.login}, user password {data.password}"')
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

    # Переход в редактирование информации через кнопку "настройка"
    def update_user(self):
        self.click_element(self.user_menu())
        self.click_element(self.about_user())
        self.click_element(self.edit_profile())

    # Переход в редактирование информации через кнопку "о пользователе"
    def update_user_2(self):
        self.click_element(self.user_menu())
        self.click_element(self.about_user_2())
        self.find_element(UserPageLocators.EDIT_INFO)

    # Находим элемент имя
    def firstname_input(self):
        return self.find_element(UserPageLocators.FIRST_NAME)

    # Находим элемент фамилия
    def lastname_input(self):
        return self.find_element(UserPageLocators.LAST_NAME)

    # Находим элемент email
    def input_email(self):
        return self.find_element(UserPageLocators.EMAIL)

    def mood_profile_input(self):
        return self.find_element(UserPageLocators.MOODLE_NET_PROFILE)

    def city_input(self):
        return self.find_element(UserPageLocators.CITY_INPUT)

    def is_change_2(self) -> bool:
        self.find_elements(UserPageLocators.IS_CHANGE)
        element = self.find_elements(UserPageLocators.IS_CHANGE)
        if len(element) > 0:
            return True
        return False

    def is_change(self):
        return self.find_element(UserPageLocators.IS_CHANGE).text

    def country_select(self) -> WebElement:
        country_select = self.find_select_element(
            UserPageLocators.COUNTRY_SELECT
        )
        return country_select

    def timezone_select(self) -> WebElement:
        timezone_select = self.find_select_element(
            UserPageLocators.TIMEZONE_SELECT
        )
        return timezone_select

    def description_input(self):
        return self.find_element(UserPageLocators.DESCRIPTION)
    # Вкладка загрузки изображения
    def moodle_picture(self):
        return self.find_element(UserPageLocators.MOODLE_PICTURE)

    def input_picture(self):
        return self.find_element(UserPageLocators.INPUT_PICTURE)

    def alt_picture(self):
        return self.find_element(UserPageLocators.ALT_PICTURE)

    # Дополнительная информация об имени.
    def additional_inf(self):
        return self.find_element(UserPageLocators.ADDITIONAL_INF)

    def first_fonetic_name(self):
        return self.find_element(UserPageLocators.FIRST_FONETIC_NAME)

    def last_fonetic_name(self):
        return self.find_element(UserPageLocators.LAST_FONETIC_NAME)

    def middle_name(self):
        return self.find_element(UserPageLocators.MIDDLE_NAME)

    def alter_name(self):
        return self.find_element(UserPageLocators.ALTER_NAME)

    # Интересы.
    def moodle_interest(self):
        return self.find_element(UserPageLocators.MOODLE_INTEREST)

    def form_autocomplite(self):
        return self.find_element(UserPageLocators.FORM_AUTOCOMPLIT)

    # Вкладка необязательное.

    def click_optional(self):
        return self.find_element(UserPageLocators.OPTIONAL)

    def id_number(self):
        return self.find_element(UserPageLocators.ID_NUMBER)

    def institution(self):
        return self.find_element(UserPageLocators.INSTITUTION)

    def departament(self):
        return self.find_element(UserPageLocators.DEPARTAMENT)

    def phone_1(self):
        return self.find_element(UserPageLocators.PHONE_1)

    def phone_2(self):
        return self.find_element(UserPageLocators.PHONE_2)

    def address(self):
        return self.find_element(UserPageLocators.ADDRESS)


    # Находим элемент сохранить данные
    def submit_button_prof(self):
        return self.find_element(UserPageLocators.SUBMIT)

    def submit_changes(self):
        self.click_element(self.submit_button_prof())

    def open_all_sections(self):
        return self.find_element(UserPageLocators.OPEN_WIN)

    def edit_personal_data(self, personal_data: PersonalData):
        #self.click_element(self.open_all_sections())
        time.sleep(5)
        self.fill_element(self.firstname_input(), personal_data.firstname)
        self.fill_element(self.lastname_input(), personal_data.lastname)
        self.fill_element(self.input_email(), personal_data.user_email)
        self.fill_element(self.mood_profile_input(), personal_data.moodle_net_profile)
        self.fill_element(self.city_input(), personal_data.city)
        self.select_value(self.country_select(),personal_data.country_code)
        self.select_value(self.timezone_select(), personal_data.timezone)
        self.fill_element(self.description_input(), personal_data.about)
        #кликаем на кнопку изображение пользователя
        #self.click_element(self.moodle_picture())
        #self.fill_element(self.input_picture(), personal_data.image_url)
        #self.fill_element(self.alt_picture(), personal_data.image_inf)
        self.click_element(self.additional_inf())
        self.fill_element(self.first_fonetic_name(), personal_data.image_inf)
        self.fill_element(self.last_fonetic_name(), personal_data.image_inf)
        self.fill_element(self.middle_name(), personal_data.image_inf)
        self.fill_element(self.alter_name(), personal_data.image_inf)
        self.click_element(self.moodle_interest())
        self.fill_element(self.form_autocomplite(), personal_data.image_inf)
        self.click_element(self.click_optional())
        self.fill_element(self.id_number(), personal_data.image_inf)
        self.fill_element(self.institution(), personal_data.image_inf)
        self.fill_element(self.departament(), personal_data.image_inf)
        self.fill_element(self.phone_1(), personal_data.image_inf)
        self.fill_element(self.phone_2(), personal_data.image_inf)
        self.fill_element(self.address(), personal_data.image_inf)
        self.submit_changes()


