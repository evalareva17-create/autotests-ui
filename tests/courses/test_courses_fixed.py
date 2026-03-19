import pytest
from playwright.sync_api import expect

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_list_page: CoursesListPage):
    # Очищаем все курсы перед тестом (delete_all_courses уже открывает страницу курсов)
    courses_list_page.delete_all_courses()
    
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
    
    # Проверяем виджет загрузки изображения без выбранной картинки
    create_course_page.check_visible_image_upload_widget(is_image_uploaded=False)
    
    # Проверяем форму создания курса с пустыми значениями и "0" в max_score/min_score
    create_course_page.check_visible_create_course_form("", "", "", "0", "0")
    
    # Проверяем тулбар упражнений
    create_course_page.create_exercises_toolbar.check_visible()
    
    # Проверяем пустой блок заданий
    create_course_page.check_visible_exercises_empty_view()
    
    # Загружаем изображение
    create_course_page.upload_preview_image("./testdata/files/image.png")
    
    # Проверяем виджет загрузки в состоянии загруженной картинки
    create_course_page.check_visible_image_upload_widget(is_image_uploaded=True)
    
    # Заполняем форму
    create_course_page.fill_create_course_form(
        title="Complete Course",
        estimated_time="2 weeks",
        description="Complete course description",
        max_score="100",
        min_score="10"
    )
    
    # Нажимаем кнопку создания курса
    create_course_page.create_course_toolbar.click_create_course_button()
    
    # Проверяем панель инструментов
    courses_list_page.toolbar_view.check_visible()
    
    # Проверяем корректность данных карточки курса
    courses_list_page.course_view.check_visible(
        index=0,
        title="Complete Course",
        max_score="100",
        min_score="10",
        estimated_time="2 weeks"
    )
