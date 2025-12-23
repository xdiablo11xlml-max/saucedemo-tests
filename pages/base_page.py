from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        """Открывает страницу по URL"""
        self.page.goto(url)

    def get_current_url(self):
        """Возвращает текущий URL"""
        return self.page.url

    def get_element_text(self, selector: str):
        """Возвращает текст элемента"""
        return self.page.locator(selector).inner_text()