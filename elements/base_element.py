from playwright.sync_api import Page, expect, Locator


class BaseElement:
    """
    Базовый класс для всех элементов PageFactory.
    Предоставляет общие методы для работы с элементами на странице.
    """

    def __init__(self, page: Page, locator: str, name: str):
        """
        Инициализация элемента

        Args:
            page: объект страницы Playwright
            locator: строка локатора (data-testid)
            name: человекочитаемое имя элемента для логирования
        """
        self.page = page
        self.locator = locator
        self.name = name

    def get_locator(self, **kwargs) -> Locator:
        """
        Получает локатор элемента с возможностью динамического форматирования

        Args:
            **kwargs: параметры для форматирования строки локатора

        Returns:
            Locator: объект локатора Playwright
        """
        locator = self.locator.format(**kwargs)
        return self.page.get_by_test_id(locator)

    def click(self, **kwargs):
        """
        Кликает по элементу

        Args:
            **kwargs: параметры для форматирования локатора
        """
        locator = self.get_locator(**kwargs)
        locator.click()

    def check_visible(self, **kwargs):
        """
        Проверяет, что элемент видим на странице

        Args:
            **kwargs: параметры для форматирования локатора
        """
        locator = self.get_locator(**kwargs)
        expect(locator).to_be_visible()

    def check_have_text(self, text: str, **kwargs):
        """
        Проверяет, что элемент содержит указанный текст

        Args:
            text: ожидаемый текст
            **kwargs: параметры для форматирования локатора
        """
        locator = self.get_locator(**kwargs)
        expect(locator).to_have_text(text)
