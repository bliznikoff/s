import json
import controlled
path_to_db = 'db.json'


def search_data():  
    name = input('Введите имя или фамилию ученика, оценки которого желаете посмотреть:  ')
    with open(path_to_db, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):  
             if name == data[i]['Name'] or name == data[i]['Surname']:
                print(data[i])       