# Используем официальный образ Python
FROM python:3.12

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY pyproject.toml poetry.lock ./

# Устанавливаем Poetry
RUN pip install poetry

# Устанавливаем зависимости
RUN poetry install --no-root

# Копируем остальные файлы проекта
COPY . .

# Устанавливаем основные зависимости
RUN poetry install
# Команда для запуска приложения
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000","--reload"]

# CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "4000", "--reload"]