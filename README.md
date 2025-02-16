# Название проекта



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