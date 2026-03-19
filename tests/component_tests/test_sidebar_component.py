import pytest
import re
from playwright.sync_api import expect

from pages.dashboard.dashboard_page import DashboardPage
from pages.courses.courses_list_page import CoursesListPage


@pytest.mark.regression
def test_sidebar_component_dashboard(chromium_page_with_state):
    """
    Тест проверяет работу SidebarComponent на странице Dashboard
    """
    page = chromium_page_with_state
    
    # Создаем экземпляр страницы
    dashboard_page = DashboardPage(page=page)
    
    # Открываем страницу дашборда
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
    
    # Проверяем видимость sidebar
    dashboard_page.sidebar.check_visible()
    
    # Проверяем остальные элементы дашборда
    dashboard_page.dashboard_toolbar.check_visible()


@pytest.mark.courses
@pytest.mark.regression
def test_sidebar_component_courses_list(chromium_page_with_state):
    """
    Тест проверяет работу SidebarComponent на странице списка курсов
    """
    page = chromium_page_with_state
    
    # Создаем экземпляр страницы
    courses_list_page = CoursesListPage(page=page)
    
    # Открываем страницу курсов
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    
    # Проверяем видимость sidebar
    courses_list_page.sidebar.check_visible()
    
    # Проверяем остальные элементы страницы
    courses_list_page.toolbar_view.check_visible()
    courses_list_page.check_visible_empty_view()


@pytest.mark.regression
def test_sidebar_navigation_dashboard_to_courses(chromium_page_with_state):
    """
    Тест проверяет навигацию с Dashboard на Courses через Sidebar
    """
    page = chromium_page_with_state
    
    # Создаем экземпляр страницы
    dashboard_page = DashboardPage(page=page)
    
    # Открываем страницу дашборда
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
    
    # Проверяем, что мы на дашборде
    expect(page).to_have_url(re.compile(r".*#/dashboard"))
    
    # Используем sidebar для перехода на страницу курсов
    dashboard_page.sidebar.click_courses()
    
    # Проверяем, что произошел переход на страницу курсов
    expect(page).to_have_url(re.compile(r".*#/courses"))


@pytest.mark.regression
def test_sidebar_navigation_courses_to_dashboard(chromium_page_with_state):
    """
    Тест проверяет навигацию с Courses на Dashboard через Sidebar
    """
    page = chromium_page_with_state
    
    # Создаем экземпляр страницы
    courses_list_page = CoursesListPage(page=page)
    
    # Открываем страницу курсов
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    
    # Проверяем, что мы на странице курсов
    expect(page).to_have_url(re.compile(r".*#/courses"))
    
    # Используем sidebar для перехода на дашборд
    courses_list_page.sidebar.click_dashboard()
    
    # Проверяем, что произошел переход на дашборд
    expect(page).to_have_url(re.compile(r".*#/dashboard"))


@pytest.mark.regression
def test_sidebar_nested_components_structure(chromium_page_with_state):
    """
    Тест демонстрирует работу вложенных компонентов в Sidebar
    """
    page = chromium_page_with_state
    
    # Создаем экземпляр страницы
    dashboard_page = DashboardPage(page=page)
    
    # Открываем страницу дашборда
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
    
    # Проверяем каждый вложенный компонент отдельно
    # Dashboard list item
    dashboard_page.sidebar.dashboard_list_item.check_visible('Dashboard')
    
    # Courses list item  
    dashboard_page.sidebar.courses_list_item.check_visible('Courses')
    
    # Logout list item
    dashboard_page.sidebar.logout_list_item.check_visible('Logout')


@pytest.mark.regression
def test_sidebar_component_reusability(chromium_page_with_state):
    """
    Тест демонстрирует переиспользование SidebarComponent на разных страницах
    """
    page = chromium_page_with_state
    
    # Проверяем sidebar на разных страницах
    pages_to_test = [
        ("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard", DashboardPage),
        ("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses", CoursesListPage)
    ]
    
    for url, page_class in pages_to_test:
        # Переходим на страницу
        page.goto(url)
        
        # Создаем экземпляр страницы
        page_instance = page_class(page=page)
        
        # Проверяем sidebar - один и тот же компонент на разных страницах
        page_instance.sidebar.check_visible()
                    
        # Дополнительная проверка: все элементы должны быть видны
        expect(page_instance.sidebar.dashboard_list_item.icon.get_locator()).to_be_visible()
        expect(page_instance.sidebar.courses_list_item.icon.get_locator()).to_be_visible()
        expect(page_instance.sidebar.logout_list_item.icon.get_locator()).to_be_visible()
