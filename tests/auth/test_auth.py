import pytest
from UI_test.common.constants import LoginConstants
from UI_test.models.auth import PersonalData, AuthData
import time

class TestAuth:
    def test_main_page(self, app):
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
        # app.open_auth_page()
        # data = AuthData(login="admin", password="Vjcrdf2!")
        # app.login.auth(data)
        assert app.login.is_auth(), "We are not auth"

    def test_auth_invalid_data(self, app, invalid_auth):
        """
        Steps
        1. Open main page
        2. Auth with invalid data
        3. Check auth result
        """
        # app.open_auth_page()
        # data = AuthData.random()
        # app.login.auth(data)
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

    def test_update_user(self, app, auth, user_info):
        """
        Steps
        1. Open main page
        2. Auth with valid data
        3. Open user info
        4. Open page update user info
        5. Input user info
        6. User info update
        """
        personal_data = PersonalData.random()
        app.login.edit_personal_data(personal_data)
        #assert app.login.is_change(), "Is not change!"
        assert LoginConstants.IS_CHANGE_INF in app.login.is_change(), "Is not change!"
