# Используем базовый образ Python
FROM python:3.12
# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл зависимостей в контейнер
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY . .

# Открываем порт 8000 для приложения Django
EXPOSE 8000

# Выполняем команду запуска сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
