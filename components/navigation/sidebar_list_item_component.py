from typing import Pattern
from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.icon_element import Icon
from elements.text_element import Text
from elements.button_element import Button


class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        # Формируем локаторы динамически
        self.icon = Icon(page, f'{identifier}-drawer-list-item-icon', 'Icon')
        self.title = Text(page, f'{identifier}-drawer-list-item-title-text', 'Title')
        self.button = Button(page, f'{identifier}-drawer-list-item-button', 'Button')

    def check_visible(self, title: str):
        self.icon.check_visible()

        self.title.check_visible()
        self.title.check_have_text(title)

        self.button.check_visible()

    def navigate(self, expected_url: Pattern[str]):
        self.button.click()
        self.check_current_url(expected_url)

    def check_current_url(self, expected_url: Pattern[str]):
        expect(self.page).to_have_url(expected_url)
