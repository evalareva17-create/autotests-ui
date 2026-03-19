from playwright.sync_api import Page, Locator, expect

from elements.base_element import BaseElement


class Input(BaseElement):
    """
    Элемент поля ввода (input).
    Предоставляет методы для работы с текстовыми полями.
    """

    def get_locator(self, **kwargs) -> Locator:
        # Получаем локатор input внутри элемента
        return super().get_locator(**kwargs).locator('input')

    def fill(self, value: str, **kwargs):
        """
        Заполняет поле ввода значением

        Args:
            value: значение для ввода
            **kwargs: параметры для форматирования локатора
        """
        locator = self.get_locator(**kwargs)
        locator.fill(value)

    def check_have_value(self, value: str, **kwargs):
        """
        Проверяет значение поля ввода

        Args:
            value: ожидаемое значение
            **kwargs: параметры для форматирования локатора
        """
        locator = self.get_locator(**kwargs)
        expect(locator).to_have_value(value)
