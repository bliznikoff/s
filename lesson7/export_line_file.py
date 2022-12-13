import json
import controlled
path_to_db = 'db.json'


def export_line():
    
    with open(path_to_db, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            with open('Export_contact_line.txt', 'a') as export:
                export.write('\n' + "".join(data[i]['Name']) + ',' + "".join(
                    data[i]['Surname']) + ',' + "".join(data[i]['Phone number']) + ',' + "".join(data[i]['Comment']))

    print('\nКонтакты успешно экспортированы в файл!\n')
    controlled.user_choice()
