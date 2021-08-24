from selenium.webdriver.common.by import By


class BasePageLocators:
    SIGN_IN = (By.CLASS_NAME, "aalink")
    USER_NAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    BUTTON = (By.ID,"loginbtn")
    SAVE_ME=(By.NAME, "rememberusername")
