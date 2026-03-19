from elements.base_element import BaseElement


class FileInput(BaseElement):
    """
    Элемент поля загрузки файлов (file input).
    Предоставляет методы для работы с загрузкой файлов.
    """

    def set_input_files(self, file: str, **kwargs):
        """
        Загружает файл в поле

        Args:
            file: путь к файлу
            **kwargs: параметры для форматирования локатора
        """
        locator = self.get_locator(**kwargs)
        locator.set_input_files(file)
