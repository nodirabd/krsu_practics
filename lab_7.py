from random import *
number = int(input("Type the ex: "))
if number == 1:
    n= int(input("size of the matrix: "))
    A=[]
    for i in range(n):
        B = [randint(-10,10) for j in range(n)]
        A.append(B)

    print("the matrix looks like: ")
    for i in range(n):
        for j in range(n):
            print(A[i][j] , end=" ")
        print()

    sum_list =[]
    count = 0 
    for i in range(n):
        for j in range(n):
            if i < j:
                sum_list.append(A[i][j])
                if A[i][j] > 0:
                    count +=1
    print(f'Sum of the elements {sum(sum_list)}')
    print(f'Number of positive values {count}')
elif number == 2:
    n = int(input("n size of the matrix: "))
    m = int(input("m size of the matrix: "))

    B = []
    for i in range(n):
        row = [randint(-10, 10) for j in range(m)]
        B.append(row)

    print("the matrix looks like: ")
    for i in range(n):
        for j in range(m):
            print(B[i][j], end="  ")
        print()

    for i in range(n):
        max_val = max(B[i])
        min_val = min(B[i])
        
        # Находим их индексы 
        max_ind = B[i].index(max_val)
        min_ind = B[i].index(min_val)
        print(f"Строка {i}: макс = {max_val}, мин = {min_val}")
        
        B[i][max_ind], B[i][0] = B[i][0], B[i][max_ind]
        B[i][min_ind], B[i][-1] = B[i][-1], B[i][min_ind]

    print() 
    print("changed matrix looks like: ")
    for i in range(n):
        for j in range(m):
            print(B[i][j], end="  ")
        print()
else:
    print("there is no other ex for this var")