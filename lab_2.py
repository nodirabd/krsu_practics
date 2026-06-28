import math
print("Solution for T1")
a, b, c = float(input("a: ")), float(input("b: ")), float(input("c: "))
while True:
    x, y = float(input("x: ")), float(input("y: "))
    if y != 0 and (y * x + c) > 0:
        break
    print("y cant be zero, and (y*x + c) should be more than 0")

t1 = round((a * x / y) + (b / y**2) * math.log10(y * x + c), 2)
print(f'The result of T1 is {t1}\n')



print("Solution for T2")
while True:
    if a == 0 or b == 0:
        print(f' a is {a}, b is {b}. a and be cant be 0')
        a, b = float(input("new value for a : ")), float(input("new value for b: "))
        continue
        
    if c**2 - b**2 < 0:
        print("error!!! (c^2 - b^2)< 0.")
        c = float(input("new value for c: "))
        continue
    k = math.sqrt(c**2 - b**2) * math.tan(a * x)
    chisl = k + 2
    znam = k - 2
    if znam == 0 or (chisl / znam) <= 0:
        print("log cant be 0 or less than 0")
        x = float(input("type another value for x: "))
        continue
    break

t2 = round((1 / (2 * a * b)) * math.log(chisl / znam), 2)
print(f'The result of T2 is {t2}')