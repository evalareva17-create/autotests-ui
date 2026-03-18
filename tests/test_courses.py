import pytest
from playwright.sync_api import expect

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


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


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(chromium_page_with_state):
    page = chromium_page_with_state
    
    # Создаем экземпляры страниц
    create_course_page = CreateCoursePage(page=page)
    courses_list_page = CoursesListPage(page=page)
    
    # Открываем страницу создания курса
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    
    # Проверяем наличие заголовка "Create course"
    create_course_page.check_visible_create_course_title()
    
    # Проверяем, что кнопка создания курса недоступна для нажатия
    create_course_page.check_disabled_create_course_button()
    
    # Убедимся, что отображается пустой блок для предпросмотра изображения
    create_course_page.check_visible_image_preview_empty_view()
    
    # Проверяем, что блок загрузки изображения отображается в состоянии, когда картинка не выбрана
    create_course_page.check_visible_image_upload_view(is_image_uploaded=False)
    
    # Проверяем, что форма создания курса отображается и содержит значения по умолчанию
    create_course_page.check_visible_create_course_form(
        title="",
        estimated_time="",
        description="",
        max_score="0",
        min_score="0"
    )
    
    # Проверяем наличие заголовка "Exercises"
    create_course_page.check_visible_exercises_title()
    
    # Проверяем наличие кнопки создания задания
    create_course_page.check_visible_create_exercise_button()
    
    # Убедимся, что отображается блок с пустыми заданиями
    create_course_page.check_visible_exercises_empty_view()
    
    # Загружаем изображение для превью курса
    create_course_page.upload_preview_image("./testdata/files/image.png")
    
    # Убедимся, что блок загрузки изображения отображает состояние, когда картинка успешно загружена
    create_course_page.check_visible_image_upload_view(is_image_uploaded=True)
    
    # Заполняем форму создания курса
    create_course_page.fill_create_course_form(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10"
    )
    
    # Нажимаем на кнопку создания курса
    create_course_page.click_create_course_button()
    
    # После создания курса проверяем наличие заголовка "Courses" на странице со списком курсов
    courses_list_page.check_visible_courses_title()
    
    # Проверяем наличие кнопки создания курса
    courses_list_page.check_visible_create_course_button()
    
    # Проверяем корректность отображаемых данных на карточке курса
    courses_list_page.check_visible_course_card(
        index=0,
        title="Playwright",
        max_score="100",
        min_score="10",
        estimated_time="2 weeks"
    )