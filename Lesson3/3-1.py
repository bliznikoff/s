# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

import os
os.system('cls')
print('Эта программа найдёт сумму элементов списка, стоящих на нечётной позиции')

def sum_not_even_index(lst):
    s = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            s += lst[i]
    print(f"Сумма равна: {s}")

lst = []
sum_not_even_index(lst)
lst = list(map(int, input("Введите числа через пробел:\n").split()))
sum_not_even_index(lst)