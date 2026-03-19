from playwright.sync_api import Locator, expect

from elements.base_element import BaseElement


class Textarea(BaseElement):
    """
    Элемент текстовой области (textarea).
    Предоставляет методы для работы с многострочными текстовыми полями.
    """

    def get_locator(self, **kwargs) -> Locator:
        # Получаем локатор textarea внутри элемента
        return super().get_locator(**kwargs).locator('textarea').first

    def fill(self, value: str, **kwargs):
        """
        Заполняет текстовую область значением

        Args:
            value: значение для ввода
            **kwargs: параметры для форматирования локатора
        """
        locator = self.get_locator(**kwargs)
        locator.fill(value)

    def check_have_value(self, value: str, **kwargs):
        """
        Проверяет значение текстовой области

        Args:
            value: ожидаемое значение
            **kwargs: параметры для форматирования локатора
        """
        locator = self.get_locator(**kwargs)
        expect(locator).to_have_value(value)
