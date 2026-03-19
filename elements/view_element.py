from playwright.sync_api import Page

from elements.base_element import BaseElement


class View(BaseElement):
    """
    Элемент контейнера/представления (view).
    Предоставляет методы для работы с контейнерами и группами элементов.
    """

    def __init__(self, page: Page, locator: str, name: str):
        super().__init__(page, locator, name)
