import pytest
from playwright.sync_api import expect, Page
from pages.login_page import LoginPage


@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize(
    "email, password",
    [
        ("user.name@gmail.com", "password"),
        ("user.name@gmail.com", "  "),
        ("  ", "password")
    ]
)
def test_wrong_email_or_password_authorization(login_page: LoginPage, email: str, password: str):
    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Заполняем форму авторизации
    login_page.fill_login_form(email=email, password=password)

    # Нажимаем кнопку "Login"
    login_page.click_login_button()

    # Проверяем наличие сообщения об ошибке
    login_page.check_visible_wrong_email_or_password_alert()


@pytest.mark.regression
@pytest.mark.authorization
def test_success_authorization(chromium_page_with_state: Page):
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
