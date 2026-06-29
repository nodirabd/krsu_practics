import math

number = int(input("Enter a number: "))
if number == 1:
    def tri_area(a, b, c):
        p = (a + b + c) / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return s

    def rect_area(a, b):
        return a * b

    def circle_area(r):
        return math.pi * (r ** 2)

    print("Choose a shape: 1 - triangle, 2 - rectangle, 3 - circle")
    choice = int(input("Your choice: "))

    if choice == 1:
        a = float(input("Side a: "))
        b = float(input("Side b: "))
        c = float(input("Side c: "))
        print(f"Area of the triangle: {tri_area(a, b, c):.2f}")
    elif choice == 2:
        a = float(input("Side a: "))
        b = float(input("Side b: "))
        print(f"Area of the rectangle: {rect_area(a, b):.2f}")
    elif choice == 3:
        r = float(input("Radius r: "))
        print(f"Area of the circle: {circle_area(r):.2f}")
    else:
        print("Invalid choice")
elif number == 2:
    def process_array(arr):
        s = sum(arr)
        avg = s / len(arr)
        return s, avg

    arr1 = [1, 2, 3, 4, 5]
    arr2 = [10, 20, 30]
    arr3 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]

    arrays = [arr1, arr2, arr3]

    for i in range(len(arrays)):
        summa, average = process_array(arrays[i])
        print(f"Array {i+1}: Sum = {summa}, Average = {average:.2f}")
else:
    print("Invalid number")