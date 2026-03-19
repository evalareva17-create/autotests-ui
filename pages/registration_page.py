from playwright.sync_api import Page
from pages.base_page import BasePage
from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button_element import Button


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Используем компонент формы регистрации
        self.registration_form = RegistrationFormComponent(page)
        self.registration_button = Button(page, 'registration-page-registration-button', 'Registration')

    def fill_registration_form(self, email: str, username: str, password: str):
        """Заполняет форму регистрации."""
        self.registration_form.fill(email, username, password)

    def click_registration_button(self):
        """Нажимает на кнопку 'Registration'."""
        self.registration_button.click()
