import pytest
from playwright.sync_api import expect

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    # Фикстура chromium_page_with_state возвращает page с уже авторизованной сессией
    page = chromium_page_with_state

    # Открываем страницу курсов
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверяем заголовок "Courses"
    courses_title = page.locator('h6', has_text="Courses")
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text("Courses")

    # Проверяем наличие текста "There is no results"
    no_results_block = page.locator('h6', has_text="There is no results")
    expect(no_results_block).to_be_visible()
    expect(no_results_block).to_have_text("There is no results")

    # Проверяем наличие и видимость иконки
    if page.locator('svg').count() > 0:
        expect(page.locator('svg').first).to_be_visible()

    # Проверяем текст описания блока
    description_text = page.locator('p', has_text="Results from the load test pipeline will be displayed here")
    expect(description_text).to_be_visible()
    expect(description_text).to_have_text("Results from the load test pipeline will be displayed here")