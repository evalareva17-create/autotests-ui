from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    page.get_by_test_id('registration-form-email-input').locator('input').fill("user@gmail.com")
    page.get_by_test_id('registration-form-username-input').locator('input').fill("user")
    page.get_by_test_id('registration-form-password-input').locator('input').fill("pass")
    page.get_by_test_id('registration-page-registration-button').click()
    page.wait_for_timeout(2000)
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    page.wait_for_timeout(2000)
    print(page.content())
