from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    # Локаторы (Selectors)
    # Используем data-test, так как это надежнее CSS классов
    USERNAME_INPUT = "[data-test='username']"
    PASSWORD_INPUT = "[data-test='password']"
    LOGIN_BUTTON = "[data-test='login-button']"
    ERROR_MESSAGE = "[data-test='error']"
    APP_LOGO = ".app_logo" # Элемент, видимый только после входа

    def login(self, username, password):
        """Метод для заполнения полей и клика"""
        self.open(self.URL)
        if username:
            self.page.fill(self.USERNAME_INPUT, username)
        if password:
            self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)

    def get_error_text(self):
        """Получает текст ошибки при неудачном входе"""
        return self.get_element_text(self.ERROR_MESSAGE)

    def is_inventory_page_open(self):
        """Проверка, что мы перешли на внутреннюю страницу"""
        # Проверяем URL и наличие логотипа
        return "inventory.html" in self.get_current_url() and self.page.is_visible(self.APP_LOGO)