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

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        """
        Получает локатор элемента с возможностью динамического форматирования

        Args:
            nth: индекс элемента (для списков)
            **kwargs: параметры для форматирования строки локатора

        Returns:
            Locator: объект локатора Playwright
        """
        locator = self.locator.format(**kwargs)
        return self.page.get_by_test_id(locator).nth(nth)

    def click(self, nth: int = 0, **kwargs):
        """
        Кликает по элементу

        Args:
            nth: индекс элемента (для списков)
            **kwargs: параметры для форматирования локатора
        """
        locator = self.get_locator(nth, **kwargs)
        locator.click()

    def check_visible(self, nth: int = 0, **kwargs):
        """
        Проверяет, что элемент видим на странице

        Args:
            nth: индекс элемента (для списков)
            **kwargs: параметры для форматирования локатора
        """
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_be_visible()

    def check_have_text(self, text: str, nth: int = 0, **kwargs):
        """
        Проверяет, что элемент содержит указанный текст

        Args:
            text: ожидаемый текст
            nth: индекс элемента (для списков)
            **kwargs: параметры для форматирования локатора
        """
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_have_text(text)
