import pytest
from playwright.sync_api import sync_playwright, expect
import os

def test_empty_courses_list():
    with sync_playwright() as playwright:
        # Шаг 1: Открываем браузер и регистрируемся
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Открываем страницу регистрации
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        # Заполняем форму
        page.get_by_test_id('registration-form-email-input').locator('input').fill("user.testcourses@gmail.com")
        page.get_by_test_id('registration-form-username-input').locator('input').fill("user")
        page.get_by_test_id('registration-form-password-input').locator('input').fill("password")
        
        # Кликаем на регистрацию
        page.get_by_test_id('registration-page-registration-button').click()

        # Ждем редиректа на Dashboard
        dashboard_title = page.locator('//h6[contains(text(), "Dashboard") or contains(text(), "Панель управления")]')
        expect(dashboard_title).to_be_visible()

        # Сохраняем состояние сессии (storage state)
        storage_path = "state.json"
        context.storage_state(path=storage_path)

        # Закрываем первый контекст
        context.close()

        # Шаг 2: Создаем новый контекст с сохраненным состоянием
        new_context = browser.new_context(storage_state=storage_path)
        new_page = new_context.new_page()

        # Открываем страницу курсов напрямую
        new_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        # Проверяем заголовок "Courses"
        courses_title = new_page.locator('h6', has_text="Courses")
        expect(courses_title).to_be_visible()
        expect(courses_title).to_have_text("Courses")

        # Проверяем наличие текста "There is no results"
        no_results_block = new_page.locator('h6', has_text="There is no results")
        expect(no_results_block).to_be_visible()
        expect(no_results_block).to_have_text("There is no results")

        # Проверяем наличие и видимость иконки
        if new_page.locator('svg').count() > 0:
            expect(new_page.locator('svg').first).to_be_visible()

        # Проверяем текст описания блока
        description_text = new_page.locator('p', has_text="Results from the load test pipeline will be displayed here")
        expect(description_text).to_be_visible()
        expect(description_text).to_have_text("Results from the load test pipeline will be displayed here")

        # Закрываем браузер
        browser.close()
        
        # Очистка файла состояния после теста
        if os.path.exists(storage_path):
            os.remove(storage_path)