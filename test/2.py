decimal = input('Введите десятичную дробь.\n')
if ',' in decimal:
    decimal_part = decimal.split(',')[1]
    first_digit_of_dp = decimal_part[:1]
    print(first_digit_of_dp)
elif '.' in decimal:
    decimal_part = decimal.split('.')[1]
    first_digit_of_dp = decimal_part[:1]
    print(first_digit_of_dp)
else:
    print('Число не распознано как дробное.')


vvod = input().split()
s = int(vvod[0])
p = int(vvod[1])
for i in range(s+1):
    if (i * (s-i) == p):
        print(i, s-i)
        break
