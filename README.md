# Сервис рекомендаций

## Установка в PyCharm

1. **Клонируйте репозиторий**:
    ```sh
    git clone https://github.com/xa202412xa/recommendation_service_api
    cd recommendation_service_api
    ```

2. **Установите зависимости**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Настройте базу данных**:
    -- Таблица "Покупки" (UserPurchases)
    CREATE TABLE UserPurchases (
        id UUID PRIMARY KEY,
        user_id UUID,
        item_id UUID,
        category VARCHAR,
        purchase_date TIMESTAMP
    );

    -- Таблица "Товары" (Items)
    CREATE TABLE Items (
        id UUID PRIMARY KEY,
        name VARCHAR,
        category VARCHAR
    );

    -- Таблица "Рекомендации" (Recommendations)
    CREATE TABLE Recommendations (
        id UUID PRIMARY KEY,
        user_id UUID,
        item_id UUID
    );


## Запуск сервиса

1. **Запустите сервер FastAPI**:
    ```sh
    uvicorn app.main:app --reload
    ```

2. **Документация API**:
    - Откройте браузер и перейдите по адресу `http://127.0.0.1:8000/docs`, чтобы увидеть интерактивную документацию API.

## Запуск тестов

1. **Запустите тесты с использованием pytest**:
    ```sh
    pytest
    ```

## Структура проекта

- `app/`: Содержит основной код приложения.
  - `main.py`: Точка входа в приложение.
  - `models.py`: Модели SQLAlchemy.
  - `schemas.py`: Схемы Pydantic.
  - `database.py`: Конфигурация базы данных.
  - `recommendation_task.py`: Асинхронная задача для генерации рекомендаций.
- `tests/`: Содержит тесты кода.
- `requirements.txt`: Зависимости Python.
- `README.md`: Документация проекта.
