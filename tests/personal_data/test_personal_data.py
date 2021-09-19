import os.path
import time

import pytest
from common.constants import LoginConstants, PersonalDataConstants
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

    @pytest.mark.parametrize("field", ["firstname", "lastname", "user_email"])
    def test_invalid_personal_data(self, app, auth, user_info, field):
        """
        Steps
        1. Open main page
        2. Auth with valid data
        3. Open user info
        4. Open page update user info
        5. We leave one of the required fields empty:
         "firstname", "lastname" or "user_email"
        6. User info not update
        """
        personal_data = PersonalData.random()
        setattr(personal_data, field, None)
        app.personal_data.edit_required_fields(personal_data)
        assert not app.personal_data.is_change_elements(), "Is change!"
