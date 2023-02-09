# Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

num = int(input('Введите трёхзначное число: '))
if 99 < num < 1000:
    digit = 0
    sum = 0
    while num > 0:
        digit = num % 10
        sum = sum + digit
        num = num // 10
    print (f'Сумма цифр = {sum}')
else:
    print ('Введено некорректное число.')