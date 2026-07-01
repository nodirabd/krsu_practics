import numpy as np
from random import uniform
number = int(input("Type the num of the ex: "))

if number == 1:

    n = int(input("Size of the array: "))
    ar = np.array([int(input(f"type {i + 1} element: ")) for i in range(n)])

    print(f"max number of the array is {ar.max()}")
    print(f"original : {ar}  reversed : {ar[::-1]}")


elif number == 2:

    n = int(input("Size of the array: "))
    array = np.array([round(uniform(0, 1), 1) for i in range(n)])
    print("Generated array:", array)
    av = round(float(array.mean()), 1)
    array = np.where(array == 0.0, av, array)

    print(f"average is {av}")
    print(f"new array: {array}")

elif number == 3:
    text = input("type a text: ")
    words = np.array(text.split())

    if len(words) > 0:
        print(f'first word is "{words[0]}"')
    else:
        print("there is no text or there were just enters")

elif number == 4:
    lst = np.array([9, -3, 5, 0, -3])
    sum_abs = np.sum(np.abs(lst))

    print(f"previous list: {lst}")
    print(f"sum of the abs values of the list: {sum_abs}")
else:
    print("there is no other ex for this var")