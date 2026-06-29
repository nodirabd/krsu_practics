number = int(input("Type the ex: "))
if number == 1:
    info = (
        "Abdurakhmanova Nodirabegim Bakhadirovna",  
        "Bishkek",  
        18,  
        161,  
    )
    print(f'Third element of the tuple:  {info[2]}')
    print(f'Second element of the tuple:  {info[1]}')
    print(f'First three elements of the tuple:  {info[:3]}')
elif number == 2:
    countries = {
        "Kyrgyzstan": "Bishkek",
        "Kazakhstan": "Astana",
        "Uzbekistan": "Tashkent",
        "USA": "Washington",
        "Russia": "Moscow",
        "India": "New Delhi",
        "China": "Beijing"
    }

    country_dict = input("Type the name of the country to find its capital: ")
    capital_result = countries.get(country_dict)

    if capital_result is not None:
        print(f"The capital of {country_dict} is {capital_result}.")
    else:
        print("Country not found in the dictionary.")


    capital_dict = input("Type the name of the city to find its country: ")
    found_country = None

    for country, capital in countries.items():
        if capital.lower() == capital_dict.lower():
            found_country = country

    if found_country is not None:
        print(f"{capital_dict} is the capital of     {found_country}.")
    else:
        print("City not found in the list of capitals.")
elif number == 3:
    info_str = "Full Name: Abdurakhmanova Nodirabegim Bakhadirovna. Hobbies: Programming in Python and web development."

    f = open("text_1.txt", "w", encoding="utf-8")
    f.write(info_str)
    f.close()

    f = open("text_1.txt", encoding="utf-8")
    content = f.read() 
    f.close()

    print("Content of the file text_1.txt:")
    print(content)
elif number == 4:
    phone_book = {}
    FILE_NAME = "phone_book_db.txt"


    def fill_dict():
        n = int(input("Enter the number of contacts to input: "))
        for _ in range(n):
            key = input("Enter the name of the contact (key): ")
            value = input("Enter the phone number (value): ")
            phone_book[key] = value
        print("Data successfully added to the dictionary.")


    def save_to_file():
        f = open(FILE_NAME, "w", encoding="utf-8")
        for key, value in phone_book.items():
            # Записываем каждую пару в формате ключ:значение на новой строке
            f.write(f"{key}:{value}\n")
        f.close()
        print("Data successfully saved to file.")


    # 3. Считывания данных из внешнего файла
    def load_from_file():
        # Очищаем текущий словарь перед загрузкой
        phone_book.clear()
        # Читаем строки из файла
        f = open(FILE_NAME, "r", encoding="utf-8")
        lines = f.readlines()
        f.close()

        for line in lines:
            # Убираем символ переноса строки и разделяем по двоеточию
            line = line.strip()
            if line:
                parts = line.split(":")
                key = parts[0]
                value = parts[1]
                phone_book[key] = value
        print("Data successfully loaded from file.")


    # 4. Добавление/изменение информации
    def add_or_update_info():
        key = input("Enter the name of the contact: ")
        value = input("Enter the phone number: ")
        phone_book[key] = value
        print(f"Contact {key} saved.")
    # 5. Удаление информации
    def delete_info():
        key = input("Enter the name of the contact to delete: ")
        # Испольуем dict.pop()
        removed_value = phone_book.pop(key, None)
        if removed_value is not None:
            print(f"Contact {key} successfully deleted.")
        else:
            print("Contact not found.")


    # 6. Поиск информации по ключу
    def search_info():
        key = input("Enter the name to search for: ")
        value = phone_book.get(key)
        if value is not None:
            print(f"Contact found — {key}: {value}")
        else:
            print("Contact not found.")


    # 7. Сортировка информации по ключу
    def sort_and_show():
        # Для сортировки элементов словаря по ключам используют функцию sorted()
        sorted_keys = sorted(phone_book.keys())
        for key in sorted_keys:
            print(f"{key}: {phone_book[key]}")


    # Основное меню программы
    def menu():
        while True:
            print("1. Fill dictionary from keyboard")
            print("2. Save data to file")
            print("3. Read data from file")
            print("4. Add / update contact")
            print("5. Delete contact")
            print("6. Find contact by name")
            print("7. Show sorted database")
            print("0. Exit")

            choice = input("Choose an action (0-7): ")

            if choice == "1":
                fill_dict()
            elif choice == "2":
                save_to_file()
            elif choice == "3":
                load_from_file()
            elif choice == "4":
                add_or_update_info()
            elif choice == "5":
                delete_info()
            elif choice == "6":
                search_info()
            elif choice == "7":
                sort_and_show()
            elif choice == "0":
                print("Program terminated.")
                break
            else:
                print("Invalid input, please try again.")


    menu()
elif number == 5:
    source_list = [1, 2, 3, 2, 4, 3, 5]
    unique_set = set(source_list)

    print("Unique elements in the list:", unique_set)
    set_a = set([1, 2, 3, 4])
    set_b = set([3, 4, 5, 6])

    intersection_set = set_a.intersection(set_b)

    print("Intersection of sets:", intersection_set)
    set_x = set([1, 2, 3])
    set_y = set([3, 4, 5])

    union_set = set_x | set_y

    print("Union of sets:", union_set)
else:
    print("there is no other ex for this var")