import time

from selenium.webdriver.remote.webelement import WebElement
import logging
from locators.login_page_locator import BasePageLocators, UserPageLocators
from models.auth import AuthData, PersonalData
from pages.base_page import BasePage

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

    def exit_confirm(self) -> WebElement:
        return self.find_elements(BasePageLocators.EXIT_CONFIRM)

    # ________________________________________________________________________________________________
    # locators for update user information

    def about_user(self) -> WebElement:
        return self.find_element(BasePageLocators.MENU_ACTION)

    def about_user_2(self) -> WebElement:
        return self.find_element(BasePageLocators.MENU_ACTION_2)

    def edit_profile(self) -> WebElement:
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
    def firstname_input(self) -> WebElement:
        return self.find_element(UserPageLocators.FIRST_NAME)

    # Находим элемент фамилия
    def lastname_input(self) -> WebElement:
        return self.find_element(UserPageLocators.LAST_NAME)

    # Находим элемент email
    def input_email(self) -> WebElement:
        return self.find_element(UserPageLocators.EMAIL)

    def mood_profile_input(self) -> WebElement:
        return self.find_element(UserPageLocators.MOODLE_NET_PROFILE)

    def city_input(self) -> WebElement:
        return self.find_element(UserPageLocators.CITY_INPUT)

    def is_change_2(self) -> bool:
        self.find_elements(UserPageLocators.IS_CHANGE)
        element = self.find_elements(UserPageLocators.IS_CHANGE)
        if len(element) > 0:
            return True
        return False

    def is_change(self) -> str:
        return self.find_element(UserPageLocators.IS_CHANGE).text

    def country_select(self) -> WebElement:
        country_select = self.find_select_element(UserPageLocators.COUNTRY_SELECT)
        return country_select

    def timezone_select(self) -> WebElement:
        timezone_select = self.find_select_element(UserPageLocators.TIMEZONE_SELECT)
        return timezone_select

    def description_input(self) -> WebElement:
        return self.find_element(UserPageLocators.DESCRIPTION)

    # Вкладка загрузки изображения
    def moodle_picture(self) -> WebElement:
        return self.find_element(UserPageLocators.MOODLE_PICTURE)

    def input_picture(self) -> WebElement:
        return self.find_element(UserPageLocators.INPUT_PICTURE)

    def alt_picture(self) -> WebElement:
        return self.find_element(UserPageLocators.ALT_PICTURE)

    def click_input_image(self):
        return self.find_elements(UserPageLocators.BUTTON_IMAGE)

    # Дополнительная информация об имени.
    def additional_inf(self) -> WebElement:
        return self.find_element(UserPageLocators.ADDITIONAL_INF)

    def first_fonetic_name(self) -> WebElement:
        return self.find_element(UserPageLocators.FIRST_FONETIC_NAME)

    def last_fonetic_name(self) -> WebElement:
        return self.find_element(UserPageLocators.LAST_FONETIC_NAME)

    def middle_name(self) -> WebElement:
        return self.find_element(UserPageLocators.MIDDLE_NAME)

    def alter_name(self) -> WebElement:
        return self.find_element(UserPageLocators.ALTER_NAME)

    # Интересы.
    def moodle_interest(self) -> WebElement:
        """Находим элемент вкладка интересы"""
        return self.find_element(UserPageLocators.MOODLE_INTEREST)

    def form_autocomplite(self) -> WebElement:
        """Находим элемент список интересов для ввода тега"""
        return self.find_element(UserPageLocators.FORM_AUTOCOMPLIT)

    def teg_autocomplite(self):
        return self.find_element(UserPageLocators.DELETE_AUTOCOMPLIT)

    def delete_autocomplite(self):
        self.click_element(self.teg_autocomplite())

    def click_optional(self) -> WebElement:
        """Находим элемент вкладка необязательное"""
        return self.find_element(UserPageLocators.OPTIONAL)

    def id_number(self) -> WebElement:
        """Находим элемент поле индивидуальный номер"""
        return self.find_element(UserPageLocators.ID_NUMBER)

    def institution(self) -> WebElement:
        """Находим элемент поле учреждение"""
        return self.find_element(UserPageLocators.INSTITUTION)

    def departament(self) -> WebElement:
        """Находим элемент поле отдел"""
        return self.find_element(UserPageLocators.DEPARTAMENT)

    def phone_1(self) -> WebElement:
        """Находим элемент поле телефон"""
        return self.find_element(UserPageLocators.PHONE_1)

    def phone_2(self) -> WebElement:
        """Находим элемент поле мобильный телефон"""
        return self.find_element(UserPageLocators.PHONE_2)

    def address(self) -> WebElement:
        """Находим элемент поле адрес"""
        return self.find_element(UserPageLocators.ADDRESS)

    def submit_button_prof(self) -> WebElement:
        """Находим элемент обновить профиль"""
        return self.find_element(UserPageLocators.SUBMIT)

    def submit_changes(self):
        """Кликаем на элемент сохранить данные"""
        self.click_element(self.submit_button_prof())

    def button_all_sections(self) -> WebElement:
        """Находим элемент раскрыть все вкладки"""
        return self.find_element(UserPageLocators.OPEN_WIN)

    def open_all_sections(self):
        """Кликаем на элемент раскрыть все вкладки"""
        self.click_element(self.button_all_sections())

    def input_image(self):
        return self.find_elements(UserPageLocators.BUTTON_IMAGE)

    def click_image(self):
        """Находим само изображение"""
        return self.find_elements(UserPageLocators.IMAGE)

    def select_image(self):
        """Находим само изображение"""
        return self.find_element(UserPageLocators.SELECT_IMAGE)

    def input_image_name(self):
        return self.find_elements(UserPageLocators.NAME_IMAGE)

    def input_name_image(self):
        """Находим поле для ввода описания фото"""
        return self.find_element(UserPageLocators.DESCRIPTION_IMAGE)

    def click_on_button_urlimage(self):
        return self.find_element(UserPageLocators.IMAGE_DOWLOUD_URL)

    def edit_personal_data(self, personal_data: PersonalData):
        """Функция, которая обновляет данные
        пользователя (имя, фамилию, email и т.д.)"""
        self.fill_element(self.firstname_input(), personal_data.firstname)
        self.fill_element(self.lastname_input(), personal_data.lastname)
        self.fill_element(self.input_email(), personal_data.user_email)
        self.fill_element(self.mood_profile_input(), personal_data.moodle_net_profile)
        self.fill_element(self.city_input(), personal_data.city)
        self.select_value(self.country_select(), personal_data.country_code)
        self.select_value(self.timezone_select(), personal_data.timezone)
        self.fill_element(self.description_input(), personal_data.about)
        # кликаем на кнопку изображение пользователя
        self.click_element(self.input_picture())
        self.click_element(self.click_on_button_urlimage())
        self.fill_element(self.alt_picture(), personal_data.image_url)
        self.click_element(self.click_input_image()[1])
        time.sleep(2)
        self.click_element(self.click_image()[0])
        self.fill_element(self.input_image_name()[30], personal_data.image_name)
        self.click_element(self.select_image())
        time.sleep(3)
        self.click_element(self.moodle_interest())
        self.fill_element(self.form_autocomplite(), personal_data.image_inf)
        self.click_element(self.additional_inf())
        self.delete_autocomplite()
        self.fill_element(self.first_fonetic_name(), personal_data.image_inf)
        self.fill_element(self.last_fonetic_name(), personal_data.image_inf)
        self.fill_element(self.middle_name(), personal_data.image_inf)
        self.fill_element(self.alter_name(), personal_data.image_inf)
        self.click_element(self.click_optional())
        self.fill_element(self.id_number(), personal_data.image_inf)
        self.fill_element(self.institution(), personal_data.image_inf)
        self.fill_element(self.departament(), personal_data.image_inf)
        self.fill_element(self.phone_1(), personal_data.image_inf)
        self.fill_element(self.phone_2(), personal_data.image_inf)
        self.fill_element(self.address(), personal_data.image_inf)
        self.fill_element(self.input_name_image(), personal_data.about)
        self.submit_changes()
