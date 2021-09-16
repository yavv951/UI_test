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

