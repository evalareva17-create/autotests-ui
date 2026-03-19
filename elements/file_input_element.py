from elements.base_element import BaseElement


class FileInput(BaseElement):
    """
    Элемент поля загрузки файлов (file input).
    Предоставляет методы для работы с загрузкой файлов.
    """

    def set_input_files(self, file: str, nth: int = 0, **kwargs):
        """
        Загружает файл в поле

        Args:
            file: путь к файлу
            nth: индекс элемента (для списков)
            **kwargs: параметры для форматирования локатора
        """
        locator = self.get_locator(nth, **kwargs)
        locator.set_input_files(file)
