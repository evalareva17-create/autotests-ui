import os
import pytest
from playwright.sync_api import expect

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage

# Get the absolute path to the test data directory
TESTDATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'testdata', 'files')


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_list_page: CoursesListPage):
    # Открываем страницу курсов
    courses_list_page.page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    
    # Проверяем отображение компонента Navbar
    courses_list_page.navbar.check_visible("fixture_user")
    
    # Проверяем отображение компонента Sidebar
    courses_list_page.sidebar.check_visible()
    
    # Проверяем панель инструментов (заголовок и кнопку создания курса)
    courses_list_page.toolbar_view.check_visible()
    
    # Проверяем пустой список курсов
    courses_list_page.check_visible_empty_view()


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(chromium_page_with_state):
    page = chromium_page_with_state
    
    # Создаем экземпляры страниц
    create_course_page = CreateCoursePage(page=page)
    courses_list_page = CoursesListPage(page=page)
    
    # Открываем страницу создания курса
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    
    # Проверяем тулбар создания курса (заголовок и кнопка disabled)
    create_course_page.create_course_toolbar.check_visible(is_create_course_disabled=True)
    
    # Проверяем, что виджет загрузки изображения отображается в состоянии, когда картинка не выбрана
    create_course_page.check_visible_image_upload_widget(is_image_uploaded=False)
    
    # Проверяем, что форма создания курса отображается и содержит значения по умолчанию
    create_course_page.check_visible_create_course_form(
        title="",
        estimated_time="",
        description="",
        max_score="0",
        min_score="0"
    )
    
    # Проверяем тулбар упражнений
    create_course_page.create_exercises_toolbar.check_visible()
    
    # Убедимся, что отображается блок с пустыми заданиями
    create_course_page.check_visible_exercises_empty_view()
    
    # Загружаем изображение для превью курса
    create_course_page.upload_preview_image(os.path.join(TESTDATA_DIR, "image.png"))
    
    # Убедимся, что виджет загрузки изображения отображает состояние, когда картинка успешно загружена
    create_course_page.check_visible_image_upload_widget(is_image_uploaded=True)
    
    # Заполняем форму создания курса
    create_course_page.fill_create_course_form(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10"
    )
    
    # Нажимаем на кнопку создания курса
    create_course_page.create_course_toolbar.click_create_course_button()
    
    # После создания курса проверяем панель инструментов
    courses_list_page.toolbar_view.check_visible()
    
    # Проверяем корректность отображаемых данных на карточке курса
    courses_list_page.course_view.check_visible(
        index=0,
        title="Playwright",
        max_score="100",
        min_score="10",
        estimated_time="2 weeks"
    )