import json
import controlled
path_to_db = 'db.json'


def export_txt():
    
    with open(path_to_db, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            with open('Export_student.txt', 'a') as export:
                export.write('\n' + "".join(data[i]['Name']) + '\n ' + "".join(
                    data[i]['Surname']) + '\n ' + "".join(data[i]['Class']) + '\n ' + "".join(
                        data[i]['Physics'])  + '\n' + "".join(data[i]['Russian']) +'\n' +  "".join(
                            data[i]['Mathematics']))
    print('\nКонтакты успешно экспортированы в файл!\n')
    controlled.user_choice()
def export_cvs():
    with open(path_to_db, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            with open('Export_student.cvs', 'a') as export:
                export.write('\n' + "".join(data[i]['Name']) +  "".join(
                    data[i]['Surname'])  + "".join(data[i]['Class'])  + "".join(
                        data[i]['Physics']) + "".join(data[i]['Russian']) + "".join(data[i]['Mathematics']))

    print('\nКонтакты успешно экспортированы в файл!\n')
    controlled.user_choice()   
