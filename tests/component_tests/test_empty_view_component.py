import pytest
from playwright.sync_api import expect

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
def test_empty_view_component_courses_list(chromium_page_with_state):
    """
    Тест проверяет работу EmptyViewComponent на странице списка курсов
    """
    page = chromium_page_with_state
    
    # Создаем экземпляр страницы
    courses_list_page = CoursesListPage(page=page)
    
    # Очищаем все курсы перед тестом
    courses_list_page.delete_all_courses()
    
    # Открываем страницу курсов
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    
    # Проверяем отображение Empty View через компонент
    courses_list_page.empty_view.check_visible(
        title='There is no results',
        description='Results from the load test pipeline will be displayed here'
    )
    
    # Проверяем, что метод страницы тоже работает
    courses_list_page.check_visible_empty_view()


@pytest.mark.courses
@pytest.mark.regression
def test_empty_view_component_create_course_preview(chromium_page_with_state):
    """
    Тест проверяет работу EmptyViewComponent для превью изображения на странице создания курса
    """
    page = chromium_page_with_state
    
    # Создаем экземпляр страницы
    create_course_page = CreateCoursePage(page=page)
    
    # Открываем страницу создания курса
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    
    # Проверяем отображение Empty View для превью изображения через компонент
    create_course_page.image_upload_widget.preview_empty_view.check_visible(
        title='No image selected',
        description='Preview of selected image will be displayed here'
    )
    
    # Проверяем, что метод страницы тоже работает (через виджет загрузки изображения)
    create_course_page.check_visible_image_upload_widget(is_image_uploaded=False)


@pytest.mark.courses
@pytest.mark.regression
def test_empty_view_component_create_course_exercises(chromium_page_with_state):
    """
    Тест проверяет работу EmptyViewComponent для упражнений на странице создания курса
    """
    page = chromium_page_with_state
    
    # Создаем экземпляр страницы
    create_course_page = CreateCoursePage(page=page)
    
    # Открываем страницу создания курса
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    
    # Проверяем отображение Empty View для упражнений через компонент
    create_course_page.exercises_empty_view.check_visible(
        title='There is no exercises',
        description='Click on "Create exercise" button to create new exercise'
    )
    
    # Проверяем, что метод страницы тоже работает
    create_course_page.check_visible_exercises_empty_view()


@pytest.mark.regression
def test_empty_view_component_reusability(chromium_page_with_state):
    """
    Тест демонстрирует переиспользование EmptyViewComponent на разных страницах
    """
    page = chromium_page_with_state
    
    # Проверяем EmptyView на разных страницах с разными идентификаторами
    empty_view_tests = [
        {
            'url': 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses',
            'component_getter': lambda: CoursesListPage(page).empty_view,
            'expected_title': 'There is no results',
            'expected_description': 'Results from the load test pipeline will be displayed here'
        },
        {
            'url': 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create',
            'component_getter': lambda: CreateCoursePage(page).image_upload_widget.preview_empty_view,
            'expected_title': 'No image selected',
            'expected_description': 'Preview of selected image will be displayed here'
        },
        {
            'url': 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create',
            'component_getter': lambda: CreateCoursePage(page).exercises_empty_view,
            'expected_title': 'There is no exercises',
            'expected_description': 'Click on "Create exercise" button to create new exercise'
        }
    ]
    
    for test_case in empty_view_tests:
        # Переходим на страницу
        page.goto(test_case['url'])
        
        # Получаем компонент
        empty_view_component = test_case['component_getter']()
        
        # Проверяем компонент
        empty_view_component.check_visible(
            title=test_case['expected_title'],
            description=test_case['expected_description']
        )


@pytest.mark.regression
def test_empty_view_component_structure(chromium_page_with_state):
    """
    Тест демонстрирует структуру EmptyViewComponent
    """
    page = chromium_page_with_state
    
    # Создаем экземпляр страницы
    courses_list_page = CoursesListPage(page=page)
    
    # Открываем страницу курсов
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    
    # Проверяем каждый элемент компонента отдельно
    empty_view = courses_list_page.empty_view
    
    # Проверяем иконку
    expect(empty_view.icon.get_locator()).to_be_visible()
    
    # Проверяем заголовок
    expect(empty_view.title.get_locator()).to_be_visible()
    expect(empty_view.title.get_locator()).to_have_text('There is no results')
    
    # Проверяем описание
    expect(empty_view.description.get_locator()).to_be_visible()
    expect(empty_view.description.get_locator()).to_have_text('Results from the load test pipeline will be displayed here')


@pytest.mark.regression
def test_empty_view_component_with_page_objects(chromium_page_with_state):
    """
    Тест демонстрирует интеграцию EmptyViewComponent с Page Objects
    """
    page = chromium_page_with_state
    
    # Создаем экземпляры страниц
    courses_list_page = CoursesListPage(page=page)
    create_course_page = CreateCoursePage(page=page)
    
    # Проверяем на странице курсов
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    
    # Используем Page Object с интегрированным EmptyViewComponent
    courses_list_page.check_visible_empty_view()
    
    # Проверяем на странице создания курса
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    
    # Используем Page Object с интегрированными EmptyViewComponent
    create_course_page.check_visible_image_upload_widget(is_image_uploaded=False)
    create_course_page.check_visible_exercises_empty_view()
