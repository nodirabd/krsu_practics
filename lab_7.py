import numpy as np

number = int(input("Type the ex: "))

if number == 1:
    n = int(input("size of the matrix: "))

    A = np.random.randint(-10, 11, size=(n, n))

    print("the matrix looks like: ")
    for i in range(n):
        for j in range(n):
            print(A[i][j], end="\t")
        print()

    sum_list = []
    count = 0
    for i in range(n):
        for j in range(n):
            if i < j:
                val = A[i][j]
                sum_list.append(val)
                if val > 0:
                    count += 1

    print(f'Sum of the elements {sum(sum_list)}')
    print(f'Number of positive values {count}')

elif number == 2:
    n = int(input("n size of the matrix: "))
    m = int(input("m size of the matrix: "))

    B = np.random.randint(-10, 11, size=(n, m))

    print("the matrix looks like: ")
    for i in range(n):
        for j in range(m):
            print(B[i][j], end="\t")
        print()
    print()
    for i in range(n):
        row = B[i]
        max_val = np.max(row)
        min_val = np.min(row)

        max_ind = np.argmax(row)
        min_ind = np.argmin(row)

        print(f"Строка {i}: макс = {max_val}, мин = {min_val}")

        B[i][0], B[i][max_ind] = B[i][max_ind], B[i][0]

        min_ind = np.argmin(B[i])

        B[i][-1], B[i][min_ind] = B[i][min_ind], B[i][-1]

    print()
    print("changed matrix looks like: ")
    for i in range(n):
        for j in range(m):
            print(B[i][j], end="\t")
        print()
else:
    print("there is no other ex for this var")