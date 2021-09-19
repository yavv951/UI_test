from selenium.webdriver.remote.webelement import WebElement
from locators.login_page_locator import BasePageLocators
from locators.personal_page_locator import UserPageLocators
from models.auth import PersonalData
from pages.base_page import BasePage


class PersonalDataPage(BasePage):
    def user_menu(self) -> WebElement:
        return self.find_element(BasePageLocators.USER_MENU)

    def about_user(self) -> WebElement:
        return self.find_element(BasePageLocators.MENU_ACTION)

    def about_user_2(self) -> WebElement:
        return self.find_element(BasePageLocators.MENU_ACTION_2)

    def edit_profile(self) -> WebElement:
        return self.find_element(UserPageLocators.EDIT_INFO)

    def update_user(self):
        """
        Функция перехода в редактирование
        информации через кнопку "настройка"
        """
        self.click_element(self.user_menu())
        self.click_element(self.about_user())
        self.click_element(self.edit_profile())

    def update_user_2(self):
        """
        Функция перехода Переход в редактирование
        информации через кнопку "о пользователе"
        """
        self.click_element(self.user_menu())
        self.click_element(self.about_user_2())
        self.find_element(UserPageLocators.EDIT_INFO)

    def firstname_input(self) -> WebElement:
        """Функция нахождения элемента поля имя"""
        return self.find_element(UserPageLocators.FIRST_NAME)

    def lastname_input(self) -> WebElement:
        """Функция нахождения элемента поля фамилия"""
        return self.find_element(UserPageLocators.LAST_NAME)

    def input_email(self) -> WebElement:
        """Функция нахождения элемента поля email"""
        return self.find_element(UserPageLocators.EMAIL)

    def mood_profile_input(self) -> WebElement:
        """Функция нахождения элемента поля - Профиль MoodleNet."""
        return self.find_element(UserPageLocators.MOODLE_NET_PROFILE)

    def city_input(self) -> WebElement:
        """Функция нахождения элемента поля город."""
        return self.find_element(UserPageLocators.CITY_INPUT)

    def is_change(self) -> str:
        """Функция отображения надписи - изменения сохранены"""
        return self.find_element(UserPageLocators.IS_CHANGE).text

    def is_change_elements(self) -> WebElement:
        """Функция отображения надписи - изменения сохранены в виде списка"""
        return self.find_elements(UserPageLocators.IS_CHANGE)

    def country_select(self) -> WebElement:
        country_select = self.find_select_element(UserPageLocators.COUNTRY_SELECT)
        return country_select

    def timezone_select(self) -> WebElement:
        timezone_select = self.find_select_element(UserPageLocators.TIMEZONE_SELECT)
        return timezone_select

    def description_input(self) -> WebElement:
        return self.find_element(UserPageLocators.DESCRIPTION)

    def moodle_picture(self) -> WebElement:
        """Находим элемент вкладка - Вкладка загрузки изображения."""
        return self.find_element(UserPageLocators.MOODLE_PICTURE)

    def input_picture(self) -> WebElement:
        return self.find_clickable_element(UserPageLocators.INPUT_PICTURE)

    def alt_picture(self) -> WebElement:
        return self.find_clickable_element(UserPageLocators.ALT_PICTURE)

    def click_input_image(self) -> WebElement:
        return self.find_clickable_element(UserPageLocators.BUTTON_IMAGE)

    def additional_inf(self) -> WebElement:
        """Находим элемент вкладка - Дополнительная информация об имени."""
        return self.find_clickable_element(UserPageLocators.ADDITIONAL_INF)

    def first_fonetic_name(self) -> WebElement:
        return self.find_clickable_element(UserPageLocators.FIRST_FONETIC_NAME)

    def last_fonetic_name(self) -> WebElement:
        return self.find_clickable_element(UserPageLocators.LAST_FONETIC_NAME)

    def middle_name(self) -> WebElement:
        return self.find_clickable_element(UserPageLocators.MIDDLE_NAME)

    def alter_name(self) -> WebElement:
        return self.find_clickable_element(UserPageLocators.ALTER_NAME)

    def moodle_interest(self) -> WebElement:
        """Находим элемент вкладка интересы."""
        return self.find_clickable_element(UserPageLocators.MOODLE_INTEREST)

    def form_autocomplite(self) -> WebElement:
        """Находим элемент список интересов для ввода тега."""
        return self.find_clickable_element(UserPageLocators.FORM_AUTOCOMPLIT)

    def teg_autocomplite(self) -> WebElement:
        """Функция для удаления тэга,находит кнопку "х"."""
        return self.find_clickable_element(UserPageLocators.DELETE_AUTOCOMPLIT)

    def delete_autocomplite(self):
        self.click_element(self.teg_autocomplite())

    def click_optional(self) -> WebElement:
        """Находим элемент вкладка необязательное."""
        return self.find_clickable_element(UserPageLocators.OPTIONAL)

    def id_number(self) -> WebElement:
        """Находим элемент поле индивидуальный номер."""
        return self.find_clickable_element(UserPageLocators.ID_NUMBER)

    def institution(self) -> WebElement:
        """Находим элемент поле учреждение."""
        return self.find_clickable_element(UserPageLocators.INSTITUTION)

    def departament(self) -> WebElement:
        """Находим элемент поле отдел."""
        return self.find_clickable_element(UserPageLocators.DEPARTAMENT)

    def phone_1(self) -> WebElement:
        """Находим элемент поле телефон."""
        return self.find_clickable_element(UserPageLocators.PHONE_1)

    def phone_2(self) -> WebElement:
        """Находим элемент поле мобильный телефон."""
        return self.find_clickable_element(UserPageLocators.PHONE_2)

    def address(self) -> WebElement:
        """Находим элемент поле адрес."""
        return self.find_clickable_element(UserPageLocators.ADDRESS)

    def submit_button_prof(self) -> WebElement:
        """Находим элемент обновить профиль."""
        return self.find_clickable_element(UserPageLocators.SUBMIT)

    def submit_changes(self):
        """Кликаем на элемент сохранить данные."""
        self.click_element(self.submit_button_prof())

    def button_all_sections(self) -> WebElement:
        """Находим элемент раскрыть все вкладки."""
        return self.find_clickable_element(UserPageLocators.OPEN_WIN)

    def open_all_sections(self):
        """Кликаем на элемент раскрыть все вкладки."""
        self.click_element(self.button_all_sections())

    def input_image(self) -> WebElement:
        """Функция, которая находит кнопку скачать."""
        return self.find_elements(UserPageLocators.BUTTON_IMAGE)

    def click_image(self) -> WebElement:
        """Функция, которая находит само изображение."""
        return self.find_clickable_element(UserPageLocators.IMAGE)

    def select_image(self) -> WebElement:
        """Находим само изображение."""
        return self.find_clickable_element(UserPageLocators.SELECT_IMAGE)

    def input_image_name(self) -> WebElement:
        return self.find_elements(UserPageLocators.NAME_IMAGE)

    def input_name_image(self) -> WebElement:
        """Функция нахождения поля для ввода описания фото."""
        return self.find_clickable_element(UserPageLocators.DESCRIPTION_IMAGE)

    def click_on_button_urlimage(self) -> WebElement:
        """Функция нахождения кнопки для загрузки изображения через URL."""
        return self.find_clickable_element(UserPageLocators.IMAGE_DOWLOUD_URL)

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
        self.click_element(self.input_picture())
        self.click_element(self.click_on_button_urlimage())
        self.fill_element(self.alt_picture(), personal_data.image_url)
        self.click_element(self.click_input_image())
        self.click_element(self.click_image())
        self.fill_element(self.input_image_name()[30], personal_data.image_name)
        self.click_element(self.select_image())
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
        self.fill_element(self.input_name_image(), personal_data.image_inf)
        self.click_element(self.submit_button_prof())

    def edit_required_fields(self, personal_data: PersonalData):
        """Дополнительная функция, для быстрой проверки заполнения информации
        без обязательных полей (имя, фамилию, email)"""
        self.fill_element(self.firstname_input(), personal_data.firstname)
        self.fill_element(self.lastname_input(), personal_data.lastname)
        self.fill_element(self.input_email(), personal_data.user_email)
        self.fill_element(self.mood_profile_input(), personal_data.moodle_net_profile)
        self.fill_element(self.city_input(), personal_data.city)
        self.select_value(self.country_select(), personal_data.country_code)
        self.select_value(self.timezone_select(), personal_data.timezone)
        self.fill_element(self.description_input(), personal_data.about)
        self.click_element(self.submit_button_prof())
