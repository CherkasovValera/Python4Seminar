# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
import math
b = abs(int(input('Введите число заначений:')))
kod = []
for i in range(2,b+1):
    for j in  range(2,i):
        if i%j==0:
            break
    else:
            kod.append(i)
            
print(kod)
