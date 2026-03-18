from playwright.sync_api import Page

from pages.base_page import BasePage
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.courses.course_view_component import CourseViewComponent
from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent
from components.views.empty_view_component import EmptyViewComponent


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Используем компоненты навигации
        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)

        # Используем компонент Empty View
        self.empty_view = EmptyViewComponent(page, 'courses-list')

        # Используем компонент карточки курса
        self.course_view = CourseViewComponent(page)

        # Используем компонент панели инструментов
        self.toolbar_view = CoursesListToolbarViewComponent(page)

    def check_visible_empty_view(self):
        self.empty_view.check_visible(
            title='There is no results',
            description='Results from the load test pipeline will be displayed here'
        )

    def navigate_to_courses_page(self):
        # Используем компонент навигации
        self.sidebar.click_courses()

    def delete_all_courses(self):
        """Удаляет все курсы со страницы"""
        # Переходим на страницу курсов
        self.page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
        
        # Пока есть курсы, удаляем их
        while True:
            try:
                # Проверяем, есть ли курсы (если есть кнопка меню)
                if self.course_view.menu.menu_button.count() == 0:
                    break
                
                # Удаляем первый курс
                self.course_view.menu.click_delete(0)
                
                # Ждем немного для обновления страницы
                self.page.wait_for_timeout(500)
            except:
                break
