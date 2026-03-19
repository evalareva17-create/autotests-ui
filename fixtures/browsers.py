import pytest
from playwright.sync_api import sync_playwright, Page, expect

from pages.authentication.registration_page import RegistrationPage


@pytest.fixture(scope="session")
def initialize_browser_state():
    """
    Регистрирует нового пользователя и сохраняет состояние браузера.
    Выполняется один раз за сессию тестирования.
    """
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Работаем с регистрационной страницей через Page Object
        registration_page = RegistrationPage(page=page)
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.registration_form.fill(email='user.fixture.test@gmail.com', username='fixture_user', password='password')
        registration_page.click_registration_button()

        dashboard_title = page.locator('//h6[contains(text(), "Dashboard") or contains(text(), "Панель управления")]')
        expect(dashboard_title).to_be_visible()

        # Сохраняем состояние сессии (storage state)
        context.storage_state(path="browser-state.json")

        context.close()
        browser.close()


@pytest.fixture(scope="function")
def chromium_page_with_state(initialize_browser_state) -> Page:
    """
    Открывает новую страницу браузера, используя сохраненное состояние из файла browser-state.json.
    """
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")
        page = context.new_page()
        
        yield page
        
        context.close()
        browser.close()

@pytest.fixture(scope="function")
def chromium_page_with_state_2(initialize_browser_state) -> Page:
    """
    Открывает ещё одну новую страницу браузера, используя сохраненное состояние из файла browser-state.json.
    """
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")
        page = context.new_page()
        
        yield page
        
        context.close()
        browser.close()

@pytest.fixture(scope="function")
def chromium_page() -> Page:
    """
    Открывает новую страницу браузера без состояния.
    """
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        yield page
        
        context.close()
        browser.close()
