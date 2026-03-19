from playwright.sync_api import expect

from elements.base_element import BaseElement


class Button(BaseElement):
    """
    Элемент кнопки (button).
    Предоставляет методы для работы с кнопками.
    """

    def check_enabled(self, **kwargs):
        """
        Проверяет, что кнопка доступна для взаимодействия

        Args:
            **kwargs: параметры для форматирования локатора
        """
        locator = self.get_locator(**kwargs)
        expect(locator).to_be_enabled()

    def check_disabled(self, **kwargs):
        """
        Проверяет, что кнопка недоступна для взаимодействия

        Args:
            **kwargs: параметры для форматирования локатора
        """
        locator = self.get_locator(**kwargs)
        expect(locator).to_be_disabled()
