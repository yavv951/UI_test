from selenium.webdriver.common.by import By


class BasePageLocators:
    PYTHON_BUTTON = (By.CLASS_NAME, "aalink")
    TEXT_LOGIN_PAGE = (By.CLASS_NAME, "col-12")
    LOGIN = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.ID, "loginbtn")
    FORM = (By.ID, "page-wrapper")
    USER_BUTTON = (By.CLASS_NAME, "userbutton")
    USER_MENU = (By.CLASS_NAME, "usermenu")
    EXIT = (By.ID, "actionmenuaction-6")
    LOGIN_ERROR = (By.ID, "loginerrormessage")
    EXIT_CONFIRM = (By.XPATH, "//button[text()='Выход']")
    MENU_ACTION = (By.ID, "actionmenuaction-5")
    MENU_ACTION_2 = (By.ID, "actionmenuaction-2")


class UserPageLocators:
    EDIT_INFO = (By.CSS_SELECTOR, "a[href*='editadvanced']")
    CHECK_BOX_SUSPENDED = (By.ID, "id_suspended")
    USER_NAME = (By.ID, "id_username")
    FIRST_NAME = (By.ID, "id_firstname")
    LAST_NAME = (By.ID, "id_lastname")
    EMAIL = (By.ID, "id_email")
    MOODLE_NET_PROFILE = (By.ID, "id_moodlenetprofile")
    CITY_INPUT = (By.ID, "id_city")
    COUNTRY_SELECT = (By.ID, "id_country")
    TIMEZONE_SELECT = (By.ID, "id_timezone")
    DESCRIPTION = (By.ID, "id_description_editoreditable")
    EMAIL_DISPLAY = (By.ID, "id_maildisplay")
    NEW_PASSWORD = (By.ID, "id_newpassword")
    SUBMIT = (By.NAME, "submitbutton")
    CHANGE = (By.ID, "yui_3_17_2_1_1630357602223_20")
