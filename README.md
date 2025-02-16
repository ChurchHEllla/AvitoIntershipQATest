# Тестовое задание Avito
Добро пожаловать. :smile_cat: :smile_cat: :smile_cat: :smile_cat: :smile_cat: 

Этот проект содержит 2 тестовых задания (1 и 2.1) для отбора на стажировку авито (Зима 2025)

## Структура проекта


Внешний вид:
```
AvitoIntershipQATest/
│   README.md  # Файл с описанием проекта и инструкциями по запуску
│   requirements.txt  # Файл, содержащий список зависимостей проекта
│   task_1.md #Файл с описанием багов к 1-му заданию
│   TESTCASES.ms #Файл с описанием тест-кейсов для 2-го задания
│   BUGS.md #Файл с описанием багов для 2-го задания
|
├───task_21/  # Директория для кода автоматизации тестов 2-го задания      
│
├───task_1_screenshorts/  # Директория для скриншотов багов к 1-му заданию
│     
├───data/  # Директория для хранения данных, необходимых для автоматизированного тестирования
```

## Требования

- Python 3.7 или выше
- pip (обычно устанавливается вместе с Python)

## Инструкция по запуску

1. Клонируйте репозиторий:
```
git clone https://github.com/ChurchHEllla/AvitoIntershipQATest
```
или скачайте [zip файл](https://github.com//ChurchHEllla/AvitoIntershipQATest/archive/refs/heads/main.zip) с проектом

2. Создайте виртуальное окружение:
```
python -m venv venv
```
3. Активируйте виртуальное окружение:
- Для Windows:
```
venv\Scripts\activate
```
- Для macOS и Linux:
```
source venv/bin/activate
```

4. Установите зависимости:
```
pip install -r requirements.txt
```
5. Запустите тесты:
```
pytest -v
```