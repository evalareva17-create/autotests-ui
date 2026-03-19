from playwright.sync_api import expect

from elements.base_element import BaseElement


class Button(BaseElement):
    """
    Элемент кнопки (button).
    Предоставляет методы для работы с кнопками.
    """

    def check_enabled(self, nth: int = 0, **kwargs):
        """
        Проверяет, что кнопка доступна для взаимодействия

        Args:
            nth: индекс элемента (для списков)
            **kwargs: параметры для форматирования локатора
        """
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_be_enabled()

    def check_disabled(self, nth: int = 0, **kwargs):
        """
        Проверяет, что кнопка недоступна для взаимодействия

        Args:
            nth: индекс элемента (для списков)
            **kwargs: параметры для форматирования локатора
        """
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_be_disabled()
