import pytest
from playwright.sync_api import sync_playwright, Page, expect

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

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        page.get_by_test_id('registration-form-email-input').locator('input').fill("user.fixture.test@gmail.com")
        page.get_by_test_id('registration-form-username-input').locator('input').fill("fixture_user")
        page.get_by_test_id('registration-form-password-input').locator('input').fill("password")
        
        page.get_by_test_id('registration-page-registration-button').click()

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
