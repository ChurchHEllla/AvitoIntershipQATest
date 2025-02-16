import json
# Класс для чтения JSON-файлов и преобразования их в словарь

class JsonToDict:
# Конструктор класса, который загружает данные из JSON-файла

    def __init__(self, filePath):
         with open(filePath, 'r', encoding='utf-8') as file:
            self.data = json.load(file)
    # Метод для получения словаря из списка по  ключу и уникальному значению в нем
    def getElementById(self, key, id):
        for el in self.data:
            if el[key] == id:
              return el