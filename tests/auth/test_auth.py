import os.path
import pytest
from common.constants import LoginConstants, CourseDataConstants
from models.auth import AuthData, PersonalData, CourseData

current_dir = os.path.dirname(__file__)
user_images_directory = os.path.join(current_dir, "user_images")


class TestAuth:

    def test_login_page(self, app):
        """
        Steps
        1. Open main page
        2. CLick on course
        """
        app.open_main_page()
        app.login.go_on_login_page()
        assert app.login.login_page_y(), "We are not in login page"

    def test_auth_valid_data(self, app, auth):
        """
        Steps
        1. Open main page
        2. Auth with valid data
        3. Check auth result
        """
        assert app.login.is_auth(), "We are not auth"

    def test_auth_invalid_data(self, app, invalid_auth):
        """
        Steps
        1. Open main page
        2. Auth with invalid data
        3. Check auth result
        """
        assert LoginConstants.AUTH_ERROR == app.login.auth_login_error(), "We are auth!"

    @pytest.mark.parametrize("field", ["login", "password"])
    def test_auth_empty_data(self, app, field):
        """
        Steps
        1. Open main page
        2. Auth with empty data
        3. Check auth result
        """
        app.open_auth_page()
        data = AuthData.random()
        setattr(data, field, None)
        app.login.auth(data)
        assert LoginConstants.AUTH_ERROR == app.login.auth_login_error(), "We are auth!"

