# Напишите программу, которая по заданному номеру четверти, показывает
#  диапазон возможных координат точек в этой четверти (x и y).

import os
os.system('cls')
print('Эта программа о заданному номеру четверти, показывает диапазон возможных координат точек')
quarter = int(input("Введите номер четверти:  "))
if   quarter == 1: print(" Первая четверть: x от 0 до + ∞, y от 0 до + ∞") 
elif quarter == 2: print(" Вторая четверть: x от 0 до  - ∞, y от 0  до + ∞ ")  
elif quarter == 3: print(" Третья четверть: x от 0 до  - ∞, y от 0  до - ∞ ")
elif quarter == 4: print(" Четвертая четверть: x от 0 до  + ∞, y от 0  до - ∞ ")
else:        print("Error, try again")