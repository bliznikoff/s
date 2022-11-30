# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

import os
os.system('cls')
print('Эта программа Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.')

def get_fibonacci(n):
    fibonacci_nums = []
    a, b = 1, 1
    for i in range(n-1):
        fibonacci_nums.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n):
        fibonacci_nums.insert(0, a)
        a, b = b, a - b
    return fibonacci_nums
    
n = int(input('Введите число: '))
fibonacci_nums = get_fibonacci(n)
print(get_fibonacci(n))
print(fibonacci_nums.index(0))