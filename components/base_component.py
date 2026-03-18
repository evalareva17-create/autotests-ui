from playwright.sync_api import Page


class BaseComponent:
    """
    Базовый класс для всех Page Components.
    Предоставляет общую функциональность для компонентов.
    """
    def __init__(self, page: Page):
        self.page = page
