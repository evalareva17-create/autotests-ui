from playwright.sync_api import Page, Locator, expect

from elements.base_element import BaseElement


class Input(BaseElement):
    """
    Элемент поля ввода (input).
    Предоставляет методы для работы с текстовыми полями.
    """

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        # Получаем локатор input внутри элемента
        return super().get_locator(nth, **kwargs).locator('input')

    def fill(self, value: str, nth: int = 0, **kwargs):
        """
        Заполняет поле ввода значением

        Args:
            value: значение для ввода
            nth: индекс элемента (для списков)
            **kwargs: параметры для форматирования локатора
        """
        locator = self.get_locator(nth, **kwargs)
        locator.fill(value)

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        """
        Проверяет значение поля ввода

        Args:
            value: ожидаемое значение
            nth: индекс элемента (для списков)
            **kwargs: параметры для форматирования локатора
        """
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_have_value(value)
