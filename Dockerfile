# Используем базовый образ Python 3.12
FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

# Задаем рабочую директорию
WORKDIR /deposit_service

# Устанавливаем необходимые зависимости, включая python3 и curl
RUN apt-get update && apt-get install -y \
    curl \
    python3 \
    python3-pip \
    python3-venv \
    && apt-get clean

# Устанавливаем Poetry
RUN pip install poetry

RUN poetry config virtualenvs.create false

# Копируем только необходимые файлы для установки зависимостей
COPY pyproject.toml poetry.lock .

# Устанавливаем зависимости с помощью Poetry
RUN poetry install --no-root --no-interaction --no-ansi

# Копируем остальные файлы проекта
COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]