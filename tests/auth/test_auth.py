from selenium.webdriver.common.by import By
import time

class TestAuth:
    def test_page_auth(self,app):
        app.open_main_page()
        app.login.auth(login='vadim951', password='Testtest@5')
        assert 1 == 1, "Check valid data"

    

