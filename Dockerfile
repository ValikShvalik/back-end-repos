# Используем официальный образ Python
FROM python:3.12

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файлы requirements.txt в рабочую директорию
COPY requirements.txt /app/


RUN pip install --no-cache-dir -r requirements.txt

# Копируем оставшиеся файлы проекта в рабочую директорию
COPY back/ /app/


# Открываем порт 8000 для доступа к контейнеру
EXPOSE 8000


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
