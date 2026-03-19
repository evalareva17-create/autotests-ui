import pytest
from playwright.sync_api import expect

from pages.dashboard.dashboard_page import DashboardPage
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage


@pytest.mark.regression
def test_navbar_component_dashboard(chromium_page_with_state):
    """
    Тест проверяет работу NavbarComponent на странице Dashboard
    """
    page = chromium_page_with_state
    
    # Создаем экземпляр страницы
    dashboard_page = DashboardPage(page=page)
    
    # Открываем страницу дашборда
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
    
    # Проверяем видимость navbar с именем пользователя из фикстуры
    dashboard_page.navbar.check_visible("fixture_user")
    
    # Проверяем остальные элементы дашборда
    dashboard_page.dashboard_toolbar.check_visible()


@pytest.mark.courses
@pytest.mark.regression
def test_navbar_component_courses_list(chromium_page_with_state):
    """
    Тест проверяет работу NavbarComponent на странице списка курсов
    """
    page = chromium_page_with_state
    
    # Создаем экземпляр страницы
    courses_list_page = CoursesListPage(page=page)
    
    # Открываем страницу курсов
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    
    # Проверяем видимость navbar
    courses_list_page.navbar.check_visible("fixture_user")
    
    # Проверяем остальные элементы страницы
    courses_list_page.toolbar_view.check_visible()
    courses_list_page.check_visible_empty_view()


@pytest.mark.courses
@pytest.mark.regression
def test_navbar_component_create_course(chromium_page_with_state):
    """
    Тест проверяет работу NavbarComponent на странице создания курса
    """
    page = chromium_page_with_state
    
    # Создаем экземпляр страницы
    create_course_page = CreateCoursePage(page=page)
    
    # Открываем страницу создания курса
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    
    # Проверяем видимость navbar
    create_course_page.navbar.check_visible("fixture_user")
    
    # Проверяем остальные элементы страницы
    create_course_page.create_course_toolbar.check_visible(is_create_course_disabled=True)
    create_course_page.check_visible_create_course_form("", "", "", "0", "0")


@pytest.mark.regression
def test_navbar_component_reusability(chromium_page_with_state):
    """
    Тест демонстрирует переиспользование NavbarComponent на разных страницах
    """
    page = chromium_page_with_state
    
    # Проверяем navbar на разных страницах
    pages_to_test = [
        ("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard", DashboardPage),
        ("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses", CoursesListPage),
        ("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create", CreateCoursePage)
    ]
    
    for url, page_class in pages_to_test:
        # Переходим на страницу
        page.goto(url)
        
        # Создаем экземпляр страницы
        page_instance = page_class(page=page)
        
        # Проверяем navbar - один и тот же компонент на разных страницах
        page_instance.navbar.check_visible("fixture_user")
                    
        # Дополнительная проверка: заголовок приложения должен быть одинаковым везде
        expect(page_instance.navbar.app_title.get_locator()).to_have_text('UI Course')


@pytest.mark.regression
def test_navbar_component_composition_example(chromium_page_with_state):
    """
    Тест демонстрирует композицию компонентов в Page Object
    """
    page = chromium_page_with_state
    
    # Создаем страницу с несколькими компонентами
    courses_list_page = CoursesListPage(page=page)
    
    # Очищаем все курсы перед тестом
    courses_list_page.delete_all_courses()
    
    # Открываем страницу
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    
    # Используем несколько компонентов вместе
    # 1. Проверяем navbar
    courses_list_page.navbar.check_visible("fixture_user")
    
    # 2. Проверяем пустое состояние
    courses_list_page.check_visible_empty_view()
    
    # 3. Проверяем заголовок страницы
    courses_list_page.toolbar_view.check_visible()
    
    # Все компоненты работают независимо, но в рамках одной страницы
