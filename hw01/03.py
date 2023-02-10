# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет
# с номером. Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый,
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

num = int(input('Введите номер билета: '))
if 99999 < num < 1000000:
    a = num//1000
    first = a//100
    second = a //10 % 10
    third = a % 10
    b = num % 1000
    fourth = b//100
    fifth = b//10 % 10
    sixth = b % 10
    print('Счастливый' if (first+second+third) == (fourth+fifth+sixth) else 'Обычный')
else:
    print('Введено некорректное число.')

# ****
# num = list(map(int, list(input('Введите номер билета: '))))
# left = sum(num[0:3])
# right = sum(num[3:0])
# print('Счастливый' if left == right else 'Обычный')