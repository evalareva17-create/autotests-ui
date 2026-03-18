from playwright.sync_api import Page, expect
import re


class AdvancedTableComponent:
    """
    Пример компонента со сложной логикой - таблица с пагинацией, сортировкой и фильтрацией
    """
    def __init__(self, page: Page, table_selector: str = "table"):
        self.page = page
        self.table = page.locator(table_selector)
        self.rows = self.table.locator("tr")
        self.pagination = page.locator(".pagination")
        self.sort_headers = self.table.locator("th.sortable")
        self.filter_input = page.locator("#table-filter")
        self.next_button = self.pagination.locator("button[aria-label='Next']")
        self.prev_button = self.pagination.locator("button[aria-label='Previous']")
        self.page_info = self.pagination.locator(".page-info")

    def wait_for_data(self):
        """Ожидание загрузки данных в таблице"""
        expect(self.rows.first).to_be_visible()
        return self

    def get_total_rows(self) -> int:
        """Получить общее количество строк"""
        return self.rows.count()

    def get_row_data(self, index: int) -> list:
        """Получить данные из конкретной строки"""
        row = self.rows.nth(index)
        cells = row.locator("td")
        return [cell.text_content() for cell in cells.all()]

    def search_in_table(self, search_text: str):
        """Поиск по таблице с ожиданием результатов"""
        self.filter_input.fill(search_text)
        self.wait_for_data()
        return self

    def sort_by_column(self, column_name: str):
        """Сортировка по колонке с проверкой состояния"""
        header = self.table.locator(f"th:has-text('{column_name}')")
        header.click()
        # Ожидание применения сортировки
        expect(header).to_have_class("sorted")
        return self

    def next_page(self):
        """Переход на следующую страницу с проверкой доступности"""
        if self.next_button.is_enabled():
            self.next_button.click()
            self.wait_for_data()
        return self

    def get_pagination_info(self) -> dict:
        """Получить информацию о пагинации"""
        info_text = self.page_info.text_content()
        # Парсинг текста "Showing 1-10 of 50"
        match = re.search(r"Showing (\d+)-(\d+) of (\d+)", info_text)
        if match:
            return {
                "start": int(match.group(1)),
                "end": int(match.group(2)),
                "total": int(match.group(3))
            }
        return {}

    def verify_data_present(self, expected_data: str):
        """Проверить наличие данных в таблице"""
        expect(self.table).to_contain_text(expected_data)
        return self


class MultiStepFormComponent:
    """
    Пример компонента с многошаговой логикой и валидацией
    """
    def __init__(self, page: Page):
        self.page = page
        self.steps = ["step1", "step2", "step3"]
        self.current_step = 0
        
        # Локаторы для каждого шага
        self.step_indicators = page.locator(".step-indicator")
        self.next_button = page.locator("button:has-text('Next')")
        self.prev_button = page.locator("button:has-text('Previous')")
        self.submit_button = page.locator("button:has-text('Submit')")
        self.error_messages = page.locator(".error-message")
        
        # Поля формы для каждого шага
        self.step1_fields = {
            "name": page.locator("#name"),
            "email": page.locator("#email")
        }
        self.step2_fields = {
            "address": page.locator("#address"),
            "phone": page.locator("#phone")
        }
        self.step3_fields = {
            "password": page.locator("#password"),
            "confirm_password": page.locator("#confirm-password")
        }

    def get_current_step_fields(self):
        """Получить поля текущего шага"""
        if self.current_step == 0:
            return self.step1_fields
        elif self.current_step == 1:
            return self.step2_fields
        else:
            return self.step3_fields

    def fill_current_step(self, **kwargs):
        """Заполнить поля текущего шага"""
        fields = self.get_current_step_fields()
        for field_name, value in kwargs.items():
            if field_name in fields:
                fields[field_name].fill(value)
        return self

    def validate_current_step(self) -> bool:
        """Валидация текущего шага"""
        fields = self.get_current_step_fields()
        
        # Пример валидации email
        if "email" in fields:
            email_value = fields["email"].input_value()
            if "@" not in email_value:
                return False
        
        # Пример валидации паролей
        if self.current_step == 2:
            password = self.step3_fields["password"].input_value()
            confirm_password = self.step3_fields["confirm_password"].input_value()
            if password != confirm_password:
                return False
        
        return True

    def next_step(self):
        """Переход к следующему шагу с валидацией"""
        if not self.validate_current_step():
            raise ValueError("Current step has validation errors")
        
        if self.current_step < len(self.steps) - 1:
            self.next_button.click()
            self.current_step += 1
            self._wait_for_step_load()
        return self

    def prev_step(self):
        """Переход к предыдущему шагу"""
        if self.current_step > 0:
            self.prev_button.click()
            self.current_step -= 1
            self._wait_for_step_load()
        return self

    def _wait_for_step_load(self):
        """Ожидание загрузки шага"""
        step_indicator = self.step_indicators.nth(self.current_step)
        expect(step_indicator).to_have_class("active")

    def submit_form(self):
        """Отправка формы с финальной валидацией"""
        if not self.validate_current_step():
            raise ValueError("Form has validation errors")
        
        self.submit_button.click()
        return self

    def get_error_messages(self) -> list:
        """Получить все сообщения об ошибках"""
        return [msg.text_content() for msg in self.error_messages.all()]


class SelectComponent:
    """
    Пример компонента для переиспользуемого элемента select
    """
    def __init__(self, page: Page, selector: str):
        self.page = page
        self.select = page.locator(selector)
        self.options = self.select.locator("option")
        self.dropdown = page.locator(f"{selector} + .dropdown")

    def select_by_value(self, value: str):
        """Выбрать опцию по значению"""
        self.select.select_option(value)
        return self

    def select_by_text(self, text: str):
        """Выбрать опцию по тексту"""
        self.select.select_option({"label": text})
        return self

    def get_selected_value(self) -> str:
        """Получить выбранное значение"""
        return self.select.input_value()

    def get_selected_text(self) -> str:
        """Получить выбранный текст"""
        return self.select.locator("option:checked").text_content()

    def get_all_options(self) -> list:
        """Получить все доступные опции"""
        return [opt.text_content() for opt in self.options.all()]

    def is_disabled(self) -> bool:
        """Проверить, заблокирован ли select"""
        return self.select.is_disabled()

    def wait_for_options(self):
        """Ожидание загрузки опций"""
        expect(self.options.first).to_be_visible()
        return self


class NotificationComponent:
    """
    Пример компонента для работы с уведомлениями
    """
    def __init__(self, page: Page):
        self.page = page
        self.notifications = page.locator(".notification")
        self.success_notifications = page.locator(".notification.success")
        self.error_notifications = page.locator(".notification.error")
        self.warning_notifications = page.locator(".notification.warning")
        self.close_buttons = page.locator(".notification .close-button")

    def wait_for_notification(self, notification_type: str = "success"):
        """Ожидание появления уведомления"""
        if notification_type == "success":
            expect(self.success_notifications.first).to_be_visible()
        elif notification_type == "error":
            expect(self.error_notifications.first).to_be_visible()
        elif notification_type == "warning":
            expect(self.warning_notifications.first).to_be_visible()
        return self

    def get_notification_text(self, index: int = 0) -> str:
        """Получить текст уведомления"""
        return self.notifications.nth(index).text_content()

    def close_notification(self, index: int = 0):
        """Закрыть уведомление"""
        self.close_buttons.nth(index).click()
        return self

    def close_all_notifications(self):
        """Закрыть все уведомления"""
        count = self.close_buttons.count()
        for i in range(count):
            self.close_notification(0)  # Всегда закрываем первое, т.к. индексы сдвигаются
        return self

    def verify_notification_count(self, expected_count: int):
        """Проверить количество уведомлений"""
        expect(self.notifications).to_have_count(expected_count)
        return self

    def wait_for_notification_disappear(self, timeout: int = 5000):
        """Ожидание исчезновения уведомлений"""
        self.notifications.wait_for(state="hidden", timeout=timeout)
        return self
