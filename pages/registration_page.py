import re

from playwright.sync_api import Page
from pages.base_page import BasePage
from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button_element import Button
from elements.link_element import Link


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Используем компонент формы регистрации
        self.registration_form = RegistrationFormComponent(page)
        self.registration_button = Button(page, 'registration-page-registration-button', 'Registration')
        self.login_link = Link(page, 'registration-page-login-link', 'Login')

    def fill_registration_form(self, email: str, username: str, password: str):
        """Заполняет форму регистрации."""
        self.registration_form.fill(email, username, password)

    def click_registration_button(self):
        """Нажимает на кнопку 'Registration'."""
        self.registration_button.click()

    def click_login_link(self):
        self.login_link.click()
        # Добавили проверку
        self.check_current_url(re.compile(".*./#/auth/login"))
