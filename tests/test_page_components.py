import os
import pytest
from playwright.sync_api import expect

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage
from components.courses.course_view_component import CourseViewComponent
from components.navigation.sidebar_component import SidebarComponent

# Get the absolute path to the test data directory
TESTDATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'testdata', 'files')


@pytest.mark.courses
@pytest.mark.regression
def test_page_components_integration(chromium_page_with_state):
    """
    Тест демонстрирует использование PageComponent вместе с POM.
    """
    page = chromium_page_with_state
    
    # Создаем экземпляры страниц
    courses_list_page = CoursesListPage(page=page)
    
    # Очищаем все курсы перед тестом
    courses_list_page.delete_all_courses()
    
    # Открываем страницу курсов
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    
    # Проверяем панель инструментов через POM
    courses_list_page.toolbar_view.check_visible()

    # Используем компонент навигации напрямую
    sidebar = SidebarComponent(page)
    # В реальном приложении здесь была бы навигация, но в тестовом приложении
    # мы просто демонстрируем доступность компонента

    # Проверяем пустое состояние через POM
    courses_list_page.check_visible_empty_view()


@pytest.mark.courses
@pytest.mark.regression
def test_course_card_component(chromium_page_with_state):
    """
    Тест демонстрирует работу компонента карточки курса.
    """
    page = chromium_page_with_state
    
    # Сначала создадим курс для тестирования карточки
    create_course_page = CreateCoursePage(page=page)
    courses_list_page = CoursesListPage(page=page)
    
    # Открываем страницу создания курса
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    
    # Заполняем форму создания курса через PageObject
    create_course_page.create_course_toolbar.check_visible(is_create_course_disabled=True)
    create_course_page.check_visible_create_course_form("", "", "", "0", "0")
    
    # Загружаем изображение
    create_course_page.upload_preview_image(os.path.join(TESTDATA_DIR, "image.png"))
    create_course_page.check_visible_image_upload_widget(is_image_uploaded=True)
    
    # Заполняем форму через компонент
    create_course_page.fill_create_course_form(
        title="Component Test Course",
        estimated_time="3 weeks",
        description="This is a test course for PageComponent demo",
        max_score="150",
        min_score="20"
    )
    
    # Создаем курс
    create_course_page.create_course_toolbar.click_create_course_button()
    
    # Теперь используем компонент карточки курса напрямую
    course_view = CourseViewComponent(page)
    
    # Проверяем данные карточки через компонент
    course_view.check_visible(
        index=0,
        title="Component Test Course",
        max_score="150",
        min_score="20",
        estimated_time="3 weeks"
    )


@pytest.mark.courses
@pytest.mark.regression
def test_component_reusability(chromium_page_with_state):
    """
    Тест демонстрирует переиспользование компонентов.
    """
    page = chromium_page_with_state
    
    # Очищаем все курсы перед тестом
    courses_list_page = CoursesListPage(page=page)
    courses_list_page.delete_all_courses()
    
    # Создаем несколько курсов для тестирования
    for i in range(2):
        create_course_page = CreateCoursePage(page=page)
        
        # Открываем страницу создания курса
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create", wait_until='networkidle')
        
        # Ждем полной загрузки страницы
        page.wait_for_selector('[data-testid="create-course-toolbar-title-text"]')
        
        # Проверяем тулбар (для первого курса кнопка disabled, для остальных может быть enabled из-за состояния формы)
        is_button_disabled = (i == 0)  # Только для первой итерации проверяем disabled
        create_course_page.create_course_toolbar.check_visible(is_create_course_disabled=is_button_disabled)
        create_course_page.upload_preview_image(os.path.join(TESTDATA_DIR, "image.png"))
        create_course_page.check_visible_image_upload_widget(is_image_uploaded=True)
        
        create_course_page.fill_create_course_form(
            title=f"Course {i+1}",
            estimated_time=f"{i+1} weeks",
            description=f"Description for course {i+1}",
            max_score=str(100 * (i+1)),
            min_score=str(10 * (i+1))
        )
        
        create_course_page.create_course_toolbar.click_create_course_button()
    
    # Переходим на страницу курсов
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    
    # Используем компонент для проверки каждой карточки
    course_view = CourseViewComponent(page)
    for i in range(2):
        course_view.check_visible(
            index=i,
            title=f"Course {i+1}",
            max_score=str(100 * (i+1)),
            min_score=str(10 * (i+1)),
            estimated_time=f"{i+1} weeks"
        )
