"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты 
вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
"""

print("Введите количесвто монет")
n = int(input())
import random
list=[]
for i in range(n):
    list.append(random.randint(0,1))
print(list)

zero = 0 # решка
one = 0 # герб
i = 0 # индекс
while i < n:
    if list[i] == 0:
        zero += 1
        i += 1
    elif list[i] == 1:
        one +=1
        i += 1

if zero > one:
    print(one)
else:
    print(zero)