def digit_check():
    try:
        input_number = int(input('Введите пункт меню: \n'))
        return input_number
    except ValueError:
        print('Это должно быть число\n')
        return digit_check()