import chek
from export_in_file import export_txt
import os
os.system('cls')

def start():
    greetings = 'Привет! Это информационная система позволяющую работать с учениками школы.'

    print(f'{greetings}\n')


def menu():
    what_to_do = 'Что будем делать? Выберите соответствующую цифру в меню:'
    new_book = '0. Создать новую базу'
    new_contact = '1. Добавить ученика'
    delete_contact = '2. Удалить ученика'
    change_surname = '3. Изменить фамилию'
    give_grade_p = '4. Поставить оценку по физике'
    give_grade_m = '5. Поставить оценку по математике'
    give_grade_r = '6. Поставить оценку по русскому языку'
    export_to_file = '7. Резервное копирование'
    see_estimation = '8. Смотреть оценки ученика'
    to_exit = '9. Выход'
    print(f'{what_to_do}\n\n{new_book}\n{new_contact}\n{delete_contact}\n{change_surname}\n{give_grade_p}\n{give_grade_m}\n{give_grade_r}\n{export_to_file}\n{see_estimation}\n{to_exit}')
    return chek.digit_check()

