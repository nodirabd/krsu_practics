number= int(input("Введите номер задачи(1-4) "))
if number == 1: 
    n = int(input("Введите длину массива N: "))

    x = []
    for i in range(n):
        print("Введите", i, "элемент:")
        x.append(int(input()))


    max_element = max(x)

    print("Исходный массив:", x)
    print("Максимальный элемент:", max_element)
    #  срез [::-1]
    print("Массив в обратном порядке:", x[::-1])
elif number == 2:
    
    a = [1.5, 0.0, 3.4, 0.0, 5.1, -2.0]
    print("Исходный массив:", a)


    sum_elements = sum(a)
    count_elements = len(a)
    sr_arifm = sum_elements / count_elements
    print("Среднее арифметическое:", round(sr_arifm, 4))

    for i in range(count_elements):
        if a[i] == 0.0:
            a[i] = sr_arifm

    print("Полученный массив:", a)


elif number == 3:
    stroka = input("Введите символьную строку (словесный текст): ")
    words = stroka.split()

    if len(words) > 0:
        print("Первое слово:", words[0])
    else:
        print("Строка пуста или состоит только из пробелов.")
elif number == 4:
    lst = [9, -3, 5, 0, -3]
   
    sum_abs = sum(abs(i) for i in lst)

    print("Исходный список:", lst)
    print("Сумма абсолютных значений его элементов:", sum_abs)