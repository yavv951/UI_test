import os.path
import pytest
from common.constants import CourseDataConstants, LoginConstants
from models.auth import CourseData

current_dir = os.path.dirname(__file__)
user_images_directory = os.path.join(current_dir, "user_images")


class TestAddCourse:

    @pytest.mark.parametrize(
        "image_file",
        [
            os.path.join(user_images_directory, image)
            for image in os.listdir(user_images_directory)
        ],
    )
    def test_valid_data_add_course(self, app, auth, image_file):
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
        assert (
            app.add_course.inf_course_deleted() == inf_course_delete
        ), "Course is not deleted"
        app.add_course.click_resume_button()

    def test_invalid_data_course_creation(self, app, auth):
        """
        Steps
        1. Authorize.
        2. Go to Create Course page.
        3. Fill in fields: «Полное название курса», «Краткое название курса».
        4. Enter day, month, year for course end date (год начала,
        позже окончания курса).
        5. Click on button resume.
        """
        app.add_course.switching_adding_course()
        course_data = CourseData.random()
        app.add_course.fill_name_course(course_data)
        app.add_course.invalid_date(course_data)
        app.add_course.fill_course_description()
        app.add_course.click_submit_save()
        assert (
            app.add_course.entering_an_incorrect_date() == LoginConstants.INCORRECT_DATE
        ), "The course was added"