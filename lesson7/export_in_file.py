import json
import controlled
path_to_db = 'db.json'


def export_txt():
    
    with open(path_to_db, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            with open('Export_contact.txt', 'a') as export:
                export.write('\n' + "".join(data[i]['Name']) + '\n ' + "".join(
                    data[i]['Surname']) + '\n ' + "".join(data[i]['Phone number']) + '\n ' + "".join(data[i]['Comment']))
    print('\nКонтакты успешно экспортированы в файл!\n')
    controlled.user_choice()
