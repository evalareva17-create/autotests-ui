from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from components.navigation.navbar_component import NavbarComponent
from components.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent
from components.views.empty_view_component import EmptyViewComponent
from components.views.image_upload_widget_component import ImageUploadWidgetComponent


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Используем компоненты
        self.navbar = NavbarComponent(page)
        self.create_course_form = CreateCourseFormComponent(page)
        self.create_course_toolbar = CreateCourseToolbarViewComponent(page)
        self.create_exercises_toolbar = CreateCourseExercisesToolbarViewComponent(page)

        # Используем компоненты Empty View
        self.exercises_empty_view = EmptyViewComponent(page, 'create-course-exercises')

        # Используем компонент загрузки изображения
        self.image_upload_widget = ImageUploadWidgetComponent(page, 'create-course-preview')

        # Используем компонент формы задания
        self.create_exercise_form = CreateCourseExerciseFormComponent(page)

    def check_visible_image_upload_widget(self, is_image_uploaded: bool = False):
        self.image_upload_widget.check_visible(is_image_uploaded)

    def click_remove_image_button(self):
        self.image_upload_widget.click_remove_image_button()

    def upload_preview_image(self, file: str):
        self.image_upload_widget.upload_preview_image(file)

    def check_visible_create_course_form(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        self.create_course_form.check_visible(title, estimated_time, description, max_score, min_score)

    def fill_create_course_form(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        self.create_course_form.fill(title, estimated_time, description, max_score, min_score)

    def check_visible_exercises_empty_view(self):
        self.exercises_empty_view.check_visible(
            title='There is no exercises',
            description='Click on "Create exercise" button to create new exercise'
        )


