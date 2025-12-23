import pytest
import allure
from pages.login_page import LoginPage

@allure.feature('Авторизация')
class TestLogin:

    @allure.story('Успешный логин')
    def test_standard_user_login(self, login_page):
        # 1. Действие
        login_page.login("standard_user", "secret_sauce")
        
        # 2. Проверка (Assert)
        # Проверяем URL и наличие элемента на след. странице
        assert login_page.is_inventory_page_open(), "Пользователь не был перенаправлен на страницу товаров"

    @allure.story('Логин с неверным паролем')
    def test_invalid_password(self, login_page):
        login_page.login("standard_user", "wrong_password")
        
        error = login_page.get_error_text()
        assert "Username and password do not match" in error, "Текст ошибки не совпадает с ожидаемым"

    @allure.story('Логин заблокированного пользователя')
    def test_locked_out_user(self, login_page):
        login_page.login("locked_out_user", "secret_sauce")
        
        error = login_page.get_error_text()
        assert "Sorry, this user has been locked out" in error, "Сообщение о блокировке не отобразилось"

    @allure.story('Логин с пустыми полями')
    def test_empty_fields(self, login_page):
        login_page.login("", "")
        
        error = login_page.get_error_text()
        assert "Username is required" in error, "Ошибка об обязательном поле Username не появилась"

    @allure.story('Логин performance_glitch_user')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_performance_glitch_user(self, login_page):
        """
        Playwright автоматически ждет загрузки страницы (default timeout 30s).
        Если задержка сайта (обычно 5с для этого юзера) не превысит таймаут, тест пройдет.
        """
        login_page.login("performance_glitch_user", "secret_sauce")
        
        # Проверяем, что вход выполнен успешно, несмотря на лаг
        assert login_page.is_inventory_page_open(), "Страница не загрузилась после задержки"