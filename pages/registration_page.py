from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from components.authentication.registration_form_component import RegistrationFormComponent


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Используем компонент формы регистрации
        self.registration_form = RegistrationFormComponent(page)
        self.registration_button = page.get_by_test_id('registration-page-registration-button')

    def fill_registration_form(self, email: str, username: str, password: str):
        """Заполняет форму регистрации."""
        self.registration_form.fill(email, username, password)

    def click_registration_button(self):
        """Нажимает на кнопку 'Registration'."""
        self.registration_button.click()
