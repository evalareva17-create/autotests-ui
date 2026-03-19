from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements import Input, Button


class LoginFormComponentFactory(BaseComponent):
    """
    Компонент формы логина, реализованный с использованием PageFactory.
    Демонстрирует использование элементов Input и Button.
    """

    def __init__(self, page: Page):
        super().__init__(page)

        # Используем PageFactory элементы
        self.email_input = Input(
            page,
            locator='login-form-email-input',
            name='Email Input'
        )
        self.password_input = Input(
            page,
            locator='login-form-password-input',
            name='Password Input'
        )
        self.login_button = Button(
            page,
            locator='login-form-login-button',
            name='Login Button'
        )

    def fill(self, email: str, password: str):
        """
        Заполняет форму логина

        Args:
            email: email пользователя
            password: пароль пользователя
        """
        self.email_input.fill(email)
        self.password_input.fill(password)

    def click_login(self):
        """Кликает по кнопке логина"""
        self.login_button.click()

    def check_visible(self, email: str, password: str):
        """
        Проверяет, что форма отображается с указанными значениями

        Args:
            email: ожидаемый email
            password: ожидаемый пароль
        """
        self.email_input.check_visible()
        self.password_input.check_visible()
        self.login_button.check_visible()
