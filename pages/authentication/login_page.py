import re

from playwright.sync_api import Page

from pages.base_page import BasePage
from components.authentication.login_form_component import LoginFormComponent
from elements.button_element import Button
from elements.link_element import Link
from elements.text_element import Text


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.login_form = LoginFormComponent(page)
        self.login_button = Button(page, 'login-page-login-button', 'Login')
        self.registration_link = Link(page, 'login-page-registration-link', 'Registration')
        self.wrong_email_or_password_alert = Text(
            page, 'login-page-wrong-email-or-password-alert', 'Wrong email or password'
        )

    def fill_login_form(self, email: str, password: str):
        self.login_form.fill(email, password)

    def click_login_button(self):
        self.login_button.click()

    def click_registration_link(self):
        self.registration_link.click()
        # Добавили проверку
        self.check_current_url(re.compile(".*./#/auth/registration"))

    def check_visible_wrong_email_or_password_alert(self):
        self.wrong_email_or_password_alert.check_visible()
        self.wrong_email_or_password_alert.check_have_text('Wrong email or password')
