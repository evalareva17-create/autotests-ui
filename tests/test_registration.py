import pytest
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
    """
    Тест на успешную регистрацию пользователя.
    """
    # Переходим на страницу регистрации
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Генерируем уникальные данные для регистрации, чтобы тест был атомарным
    import time
    timestamp = int(time.time())
    email = f"user_{timestamp}@example.com"
    username = f"user_{timestamp}"
    password = "password"

    # Заполняем форму регистрации
    registration_page.fill_registration_form(email, username, password)

    # Нажимаем кнопку регистрации
    registration_page.click_registration_button()

    # Проверяем, что после регистрации виден заголовок "Dashboard"
    dashboard_page.check_dashboard_title_visible()
