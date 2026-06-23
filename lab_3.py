import math

number = int(input("Какое задание по лабу 1 или 2:"))   
if number == 1: 
 # Даны три целых числа. Выбрать из них те, которые принадлежат интервалу [1,3].
    a = int(input("Введите число a: "))
    b = int(input("Введите число b: "))
    c = int(input("Введите число c: "))

    found = False
    print("числа находящиеся в промежутке от 1 до 3: ")
    if 1 <= a <= 3:
        print(a)
        found = True

    if 1 <= b <= 3:
        print(b)
        found = True

    if 1 <= c <= 3:
        print(c)
        found = True
    if not found:
        print("данные цифры не принадлежат данному интервалу ")


elif number ==2: 
    print()
    """x^2 + |x-8|  -15<x<8
        x^3 + 4x-5   x>=8
        cos^2(x-3x^3) all other values of x"""
    
    x = int(input("Введите значение х:"))
    if -15 <x < 8:
        u=x**2+abs(x-8)
        print(f'Решение для x^2 + |x-8| = {u} ')
    elif x>=8:
        u=pow(x,3)+ 4*x -5
        print(f'Решение для x^3 + 4x-5  = {u} ')
    else: 
        u=pow(math.cos(x-3*pow(x,3)), 2)

else:
    print("нет такого задания для варианта 1  ")