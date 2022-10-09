# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.
import random, math
b = abs(int(input('Введите число заначений:')))
a = [random.randint(0,10) for _ in range(b)]
print(a)
c = []
x = 0
for i in range(len(a)):
    while x < len(a):
        if a[x] == a[i] and x != i:
            x = 0
            break
        x +=1
    else:
        c.append(a[i])
        x = 0
print(c)