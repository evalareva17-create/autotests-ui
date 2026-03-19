from playwright.sync_api import Page

from elements.base_element import BaseElement


class Text(BaseElement):
    """
    Элемент текста (text).
    Предоставляет методы для работы с текстовыми элементами (заголовки, параграфы, span и т.д.).
    """

    def __init__(self, page: Page, locator: str, name: str):
        super().__init__(page, locator, name)
