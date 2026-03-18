from playwright.sync_api import Page, expect


class CourseCardComponent:
    def __init__(self, page: Page, index: int = 0):
        self.page = page
        self.index = index
        
        # Локаторы для карточки курса по индексу
        self.course_title = page.get_by_test_id('course-widget-title-text')
        self.course_image = page.get_by_test_id('course-preview-image')
        self.course_max_score_text = page.get_by_test_id('course-max-score-info-row-view-text')
        self.course_min_score_text = page.get_by_test_id('course-min-score-info-row-view-text')
        self.course_estimated_time_text = page.get_by_test_id('course-estimated-time-info-row-view-text')
        
        # Локаторы для меню курса
        self.course_menu_button = page.get_by_test_id('course-view-menu-button')
        self.course_edit_menu_item = page.get_by_test_id('course-view-edit-menu-item')
        self.course_delete_menu_item = page.get_by_test_id('course-view-delete-menu-item')

    def check_visible_course_card(self, title: str, max_score: str, min_score: str, estimated_time: str):
        expect(self.course_image.nth(self.index)).to_be_visible()
        
        expect(self.course_title.nth(self.index)).to_be_visible()
        expect(self.course_title.nth(self.index)).to_have_text(title)
        
        expect(self.course_max_score_text.nth(self.index)).to_be_visible()
        expect(self.course_max_score_text.nth(self.index)).to_have_text(f"Max score: {max_score}")
        
        expect(self.course_min_score_text.nth(self.index)).to_be_visible()
        expect(self.course_min_score_text.nth(self.index)).to_have_text(f"Min score: {min_score}")
        
        expect(self.course_estimated_time_text.nth(self.index)).to_be_visible()
        expect(self.course_estimated_time_text.nth(self.index)).to_have_text(f"Estimated time: {estimated_time}")

    def click_edit_course(self):
        self.course_menu_button.nth(self.index).click()
        expect(self.course_edit_menu_item.nth(self.index)).to_be_visible()
        self.course_edit_menu_item.nth(self.index).click()

    def click_delete_course(self):
        self.course_menu_button.nth(self.index).click()
        expect(self.course_delete_menu_item.nth(self.index)).to_be_visible()
        self.course_delete_menu_item.nth(self.index).click()

    def get_title_text(self) -> str:
        return self.course_title.nth(self.index).text_content()

    def get_max_score_text(self) -> str:
        return self.course_max_score_text.nth(self.index).text_content()

    def get_min_score_text(self) -> str:
        return self.course_min_score_text.nth(self.index).text_content()

    def get_estimated_time_text(self) -> str:
        return self.course_estimated_time_text.nth(self.index).text_content()
