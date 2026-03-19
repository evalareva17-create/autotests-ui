import pytest
from playwright.sync_api import expect, Page

from pages.authentication.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.authorization
class TestAuthorization:
    @pytest.mark.parametrize(
        "email, password",
        [
            ("user.name@gmail.com", "password"),
            ("user.name@gmail.com", "  "),
            ("  ", "password")
        ]
    )
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

        # Заполняем форму авторизации
        login_page.fill_login_form(email=email, password=password)

        # Нажимаем кнопку "Login"
        login_page.click_login_button()

        # Проверяем наличие сообщения об ошибке
        login_page.check_visible_wrong_email_or_password_alert()

    def test_success_authorization(self, chromium_page_with_state: Page):
        login_page = LoginPage(chromium_page_with_state)
        
        # Мы ожидаем, что мы уже залогинены благодаря chromium_page_with_state
        # Ищем кнопку выхода и нажимаем ее
        # Пробуем универсальный локатор для кнопки выхода (обычно в хедере)
        logout_button = login_page.page.get_by_test_id('header-logout-button') # Попытка угадать test-id, если нет - fallback
        
        if logout_button.count() == 0:
             # Fallback локатор
             logout_button = login_page.page.locator("//button[contains(text(), 'Exit') or contains(text(), 'Выход') or contains(text(), 'Logout')]")

        if logout_button.is_visible():
            logout_button.click()
        
        # Переходим на страницу логина
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

        # Заполняем форму авторизации данными из фикстуры
        login_page.fill_login_form("user.fixture.test@gmail.com", "password")

        # Нажимаем кнопку "Login"
        login_page.click_login_button()

        # Проверяем успешный вход (наличие заголовка Dashboard)
        dashboard_title = login_page.page.locator('//h6[contains(text(), "Dashboard") or contains(text(), "Панель управления")]')
        expect(dashboard_title).to_be_visible()

    def test_successful_authorization(
            self,
            login_page: LoginPage,
            dashboard_page: DashboardPage,
            registration_page: RegistrationPage
    ):
        # Переход на страницу регистрации
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        # Заполнение формы регистрации и нажатие кнопки "Registration"
        registration_page.registration_form.fill(email="user.name@gmail.com", username="username", password="password")
        registration_page.click_registration_button()

        # Проверка видимости элементов Dashboard
        dashboard_page.dashboard_toolbar.check_visible()
        dashboard_page.navbar.check_visible("username")
        dashboard_page.sidebar.check_visible()
        # Клик по кнопке "Logout"
        dashboard_page.sidebar.click_logout()

        # Переход на страницу авторизации и авторизация
        login_page.login_form.fill(email="user.name@gmail.com", password="password")
        login_page.click_login_button()

        # Проверка элементов Dashboard после входа
        dashboard_page.dashboard_toolbar.check_visible()
        dashboard_page.navbar.check_visible("username")
        dashboard_page.sidebar.check_visible()

    def test_navigate_from_authorization_to_registration(
            self,
            login_page: LoginPage,
            registration_page: RegistrationPage
    ):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.click_registration_link()

        registration_page.registration_form.check_visible(email="", username="", password="")
