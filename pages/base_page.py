from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, app):
        self.app = app

    def find_element(self, locator, wait_time=15):
        element = WebDriverWait(self.app.driver, wait_time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )
        return element

    def find_elements(self, locator):
        return self.app.driver.find_elements(*locator)

    def fill_element(self, element, text):
        element.clear()
        if text:
            element.send_keys(text)
            return element

    def click_element(self, element):
        element.click()

    def find_select_element(self, locator):
        select_element = Select(self.find_element(locator))
        return select_element

    def select_value(self, select_element, value):
        select_element.select_by_value(value)

    def make_screenshot(self):
        return self.app.driver.get_screenshot_as_png()
