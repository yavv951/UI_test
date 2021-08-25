from UI_test.pages.login_page import LoginPage


class Application:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.login = LoginPage(self)

    def quit(self):
        self.driver.quit()

    def open_main_page(self):
        self.driver.get(self.url)


    def open_auth_page(self):
        self.driver.get(self.url + "/login/index.php")

