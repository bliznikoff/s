import add_student as ac
import user_interface as ui
import give_grade_p as ggp
import change_surname as cs
import delete_contact as dc
import give_grade_m as ggm
import export_in_file as eif
import search_data as sd
import give_grade_r as ggr

def user_choice():
    choice_num = ui.menu()
    if choice_num < 0 or choice_num > 9:
        print('\nОшибка ввода!\n\nЧисло должно соответствовать пункту меню!\n')
        user_choice()
    elif choice_num == 0:
        ac.create_json()
    elif choice_num == 1:
        ac.add_to_json()
    elif choice_num == 2:
        dc.delete_contact()
    elif choice_num == 3:
        cs.change_surname()
    elif choice_num == 4:
        ggp.give_grade_p()
    elif choice_num == 5:
        ggm.give_grade_m()
    elif choice_num == 6:
        ggr.give_grade_r()
    elif choice_num == 7:
        eif.export_txt()
        eif.export_cvs()
    elif choice_num == 8:
        sd.search_data()
    elif choice_num == 9:    
        print('\nСпасибо что пользовались нашим приложением!\n\nДо новых встреч!')
        exit()