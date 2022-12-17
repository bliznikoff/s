import json
import controlled

def create_json():
    json_data = []
    with open('db.json', 'w') as file:
        file.write(json.dumps(json_data, indent=2, ensure_ascii=False))
    controlled.user_choice()

def add_to_json():
    name = input("Введите имя: ")
    surname = input('Введите Фамилию: ')
    classs = input('Введите номер класса: ')
    estimation_p = 'Physics'
    estimation_r = 'Russian'
    estimation_m = 'Mathematics'
    json_data = {
        "Name": name,
        "Surname": surname,
        "Class": classs,
        "Physics" : estimation_p,
        "Russian" : estimation_r,
        "Mathematics" : estimation_m,
    }
    data = json.load(open("db.json"))
    data.append(json_data)
    with open("db.json", "w") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
        print('\nНовый ученик успешно добавлен!\n')
    controlled.user_choice()