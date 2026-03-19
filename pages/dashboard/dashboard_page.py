from playwright.sync_api import Page

from pages.base_page import BasePage
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from components.charts.chart_view_component import ChartViewComponent


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Используем компоненты навигации
        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)

        # Используем компонент тулбара
        self.dashboard_toolbar = DashboardToolbarViewComponent(page)

        # Используем компоненты графиков
        self.students_chart_view = ChartViewComponent(page, "students", "bar")
        self.activities_chart_view = ChartViewComponent(page, "activities", "line")
        self.courses_chart_view = ChartViewComponent(page, "courses", "pie")
        self.scores_chart_view = ChartViewComponent(page, "scores", "scatter")

    def click_dashboard_navigation(self):
        # Используем компонент навигации для перехода на дашборд
        self.sidebar.click_dashboard()
