# Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter.

import os
os.system('cls')
print('Эта программа выведет только двузначные числа.')

def double_digit():
    nums = list(map(int, input('Введите числа через пробел:').split()))
    return ' '.join(map(str, filter(lambda i: 9 < abs(i) < 100, nums)))

print(f'[{double_digit()}]')