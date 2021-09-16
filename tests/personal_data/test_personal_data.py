import os.path
import pytest
from common.constants import LoginConstants
from models.auth import PersonalData

current_dir = os.path.dirname(__file__)
user_images_directory = os.path.join(current_dir, "user_images")


@pytest.mark.personal_data
class TestPersonalData:
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
        app.personal_data.edit_personal_data(personal_data)
        assert (
            LoginConstants.IS_CHANGE_INF in app.personal_data.is_change()
        ), "Is not change!"
