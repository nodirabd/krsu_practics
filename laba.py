def my_decorator(func):
    def wrapper():
        print("Что-то делаем до вызова функции.")
        func()
        print("Что-то делаем после вызова функции.")
    return wrapper
def say_hello():
    print("Привет!")

say_hello = my_decorator(say_hello)
say_hello()
