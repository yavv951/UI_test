import logging
from pages.add_course_page import AddCoursePage
from pages.login_page import LoginPage
from pages.update_user_page import PersonalDataPage

logger = logging.getLogger("moodle")


class Application:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.login = LoginPage(self)
        self.add_course = AddCoursePage(self)
        self.personal_data = PersonalDataPage(self)

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