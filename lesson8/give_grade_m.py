import json
import controlled
path_to_db = 'db.json'

def give_grade_m():  
    name = input('Введите имя или фамилию ученика, кому ставим оценку:  ')
   
    with open(path_to_db, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):  
            if name == data[i]['Name'] or name == data[i]['Surname']:
                data[i]['Mathematics'] =data[i]['Mathematics'] + ',' + input('оценка: ')
                with open(path_to_db, 'w', encoding='UTF-8') as file:
                    json.dump(data, file, indent = 6)
    print('\nоценка поставлена!\n')
    controlled.user_choice()