number = int(input("Номер задачи 1 , 2 или 3: "))

if number == 1 :
    cost = float(input("Цена конфет за 1 кг : "))
    for i in range(2, 11):
        print(f"цена конфет за {i} кг : {cost*i} сомов")
        

elif number ==2:
    numbers = int(input("введите число для старта: "))
    total_sum = 0
    count = 0 
    while numbers != 0:
        total_sum += numbers
        count +=1
        numbers = int(input("введите след число: "))
    print(f'Сумма последовательности равна {total_sum}')
    print(f'Количество чисел в данной последовательности {count}')


elif number == 3 :
    a = int(input("Кол-во звезд на 1-й строке: "))
    b = "*"
    for i in range(a, 0, -1):
        print(b * i)
    for i in range(2, a + 1):
        print(b * i)


else:
    print("Нет такой задачи для варианта 1 ")
