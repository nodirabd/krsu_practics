from random import *

number = int(input("Type the num of the ex: "))

if number == 1:
    n = int(input("Size of the array: "))
    ar = []

    for i in range(n):
        num= int(input(f'type {i+1} element: '))
        ar.append(num)

    print(f'max number of the array is {max(ar)}')
    print(f'original : {ar}  reversed : {ar[::-1]}')

elif number == 2:
    n = int(input("Size of the array: "))
    array = [round(uniform(0, 1), 1) for i in range(n)]
    print("Сгенерированный массив:", array)
    av = round(sum(array)/len(array),1)

    for i in range(n):
        if array[i]== 0.0:
            i = av

    print(f'average is {av}')
    print(f'new array: {array}')

elif number == 3:
    stroka = input("type a text: ")
    words = stroka.split()

    if len(words) > 0:
        print(f'first word is "{words[0]}"')
    else:
        print("there is no text or there were just enters")

elif number == 4:
    lst = [9, -3, 5, 0, -3]
    sum_abs = sum(abs(i) for i in lst)

    print("previous list:", lst)
    print("sum of the abs values of the list:", sum_abs)
else:
    print("there is no other ex for this var")