import os.path
import pytest
from common.constants import LoginConstants, CourseDataConstants
from models.auth import AuthData, PersonalData, CourseData

current_dir = os.path.dirname(__file__)
user_images_directory = os.path.join(current_dir, "user_images")


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
        # assert app.login.is_change(), "Is not change!"
        assert LoginConstants.IS_CHANGE_INF in app.login.is_change(), "Is not change!"

    @pytest.mark.parametrize(
        "image_file",
        [
            os.path.join(user_images_directory, image)
            for image in os.listdir(user_images_directory)
        ],
    )
    def test_add_course(self, app, auth, image_file):
        """
        Steps
        1. Authorize.
        2. Go to Create Course page.
        3. Fill in fields: «Полное название курса», «Краткое название курса».
        4. Add icon image course.
        5. In section «Описание».
        6. In section "Формат курса" choose number in  «Количество секций».
        7. In section "Внешний вид" choose Russian or English language
            in dropdown «Принудительный язык».
        8. In section "Внешний вид" choose value
            in dropdown «Количество отображаемых объявлений».
            «Показывать журнал оценок студентам»,
             «Показывать отчеты о деятельности»,
             «Показать даты активных элементов».
        9. Click button «Сохранить и показать».
        10. Check if the created course name is in the page header.
        11. Go to https://qacoursemoodle.innopolis.university/course/management.php.
        12. Find the created course name on the page.
        13. Click delete button next to the new course name.
        14. Confirm deletion by clicking «Удалить».
        15. Check for text "{the new course name} был полностью удален".
        16. Click on button resume.
        """
        app.add_course.switching_adding_course()
        app.add_course.open_all_tabs()
        course_data = CourseData.random()
        app.add_course.fill_name_course(course_data)
        app.add_course.fill_course_description()
        app.add_course.choose_course_image_file(image_file)
        app.add_course.fill_add_rest_inf(course_data)
        app.add_course.click_submit_save()
        assert (
                app.add_course.course_name_after_add() == course_data.fullname_course
        ), "The course was not added"

        app.open_managment_page()
        app.add_course.click_delete_course()
        app.add_course.click_delete_button()

        inf_course_delete = (
            f"{course_data.shortname_course} {CourseDataConstants.DELETE_COURSE_INFORM}"
        )
        assert app.add_course.inf_course_deleted() == inf_course_delete, "Course is not deleted"
        app.add_course.click_resume_button()
