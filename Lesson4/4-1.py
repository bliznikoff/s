# Вычислить число Pi c заданной точностью d, не используя ф. round()

import math
import os
os.system('cls')
print('Эта программа выдает число Pi c заданной точностью d, не используя ф. round()')
d = int(input('Введите степень округления количество знаков после запятой  '))
pi_round = int(math.pi * 10**d) /10**d
print(pi_round)
# можно еще использовать math.ceil math.floor