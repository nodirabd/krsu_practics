import math
a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
c = float(input("Введите значение c: "))
x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))

# y cant be 0 in t1, the same solutions for a b and squared part for t2
if y == 0 or a == 0 or b == 0 or (c**2 - b**2) < 0:
    print("Недопустимые значения переменных!!!\n" 
    "Деление на ноль или корень из отрицательного числа)."
    )
else:
    lg_value = y * x + c
    if lg_value <= 0:
        print("Выражение под lg(yx+c) должно быть больше 0.")
    else:
        t1 = (a * x) / y + (b /(y**2)) * math.log10(lg_value)
        print("Результат t1: {0:.2f}".format(t1))


    num = math.sqrt(c**2 - b**2) * math.tan(a * x + 2)
    den = math.sqrt(c**2 - b**2) * math.tan(a * x - 2)

    if den == 0:
        print("Деление на ноль в аргументе логарифма.")
    elif (num / den) <= 0:
        print(
            "Аргумент натурального логарифма должен быть положительным."
        )
    else:
        t2 = (1 / (2 * a * b)) * math.log(num / den)
        print("Результат t2: {0:.2f}".format(t2))