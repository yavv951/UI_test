import logging

from pages.login_page import LoginPage

logger = logging.getLogger("moodle")


class Application:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.login = LoginPage(self)

    def quit(self):
        self.driver.quit()

    def open_main_page(self):
        logger.info("open " + self.url)
        self.driver.get(self.url)

    def open_auth_page(self):
        logger.info("open " + self.url + "/login/index.php")
        self.driver.get(self.url + "/login/index.php")

    def open_managment_page(self):
        logger.info("open " + self.url + "/course/management.php")
        self.driver.get(self.url + "/course/management.php")
