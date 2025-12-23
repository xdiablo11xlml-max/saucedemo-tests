# Используем официальный образ от Microsoft (Playwright + Python)
FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . .

# Команда по умолчанию: запуск тестов с созданием папки для allure-отчетов
CMD ["pytest", "--alluredir=allure-results"]