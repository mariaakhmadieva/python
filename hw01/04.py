# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('n = '))
m = int(input('m = '))
k = int(input('k = '))
if k > n and k > m:
    print('incorrect data.')
else:
    print ('yes' if n <= k and k%n == 0 or m <= k and k%m == 0 else 'no')