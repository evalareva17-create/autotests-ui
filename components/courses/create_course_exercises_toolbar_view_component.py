from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.text_element import Text
from elements.button_element import Button


class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.title = Text(page, 'create-course-exercises-box-toolbar-title-text', 'Title')
        self.create_exercise_button = Button(page, 'create-course-exercises-box-toolbar-create-exercise-button', 'Create Exercise')

    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text('Exercises')
        self.create_exercise_button.check_visible()

    def click_create_exercise_button(self):
        self.create_exercise_button.click()
