import json
class JsonToDict:
    def __init__(self, filePath):
         with open(filePath, 'r', encoding='utf-8') as file:
            self.data = json.load(file)
    def getElementById(self, key, id):
        for el in self.data:
            if el[key] == id:
              return el 
    def getElements(self, key):
        data_list = []  
        for el in self.data.get(key):  
            data_list.append(el["value"])  
        return data_list 
