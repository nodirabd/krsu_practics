# text = input("type a text to check: ")
# print(len(text))
# new_text=''
# goal = True
# for i in range (len(text)):
#     if text[i] != " ":
#         new_text+= text[i]
# print(new_text)

# for i in range(len(new_text)):
#     if new_text[i] == new_text[-i -1]:
#         goal
#         break
#     else:
#         goal = False
# if goal: 
#     print('goal reached')
# else:
#     print('no')
exercise_num = input("вариант задачи (1.1, 1.2, 2: )")
# first part of the first var 
if exercise_num == '1.1':
        
    text = input('напишите текст чтоб проверить наличие на букву "е" :').lower()
    count = 0
    splitted_text = text.split() 
    print(splitted_text)
    for word in splitted_text:
        if word and word[0] == 'e':
            count += 1 
    print(count)

elif exercise_num == '1.2':
    text = input('type the text to check how many words start with "e" :').lower()
    count = 0
    splitted_text = text.split() 
    print(splitted_text)
    for word in splitted_text:
        if word.startswith('e'):
            count += 1
    print(count)

# second 
elif exercise_num == '2':
    """2. Ввести с клавиатуры символьную строку и заменить в 
    ней все буквы «а» на «б» и все буквы «б» на «а» 
    (заглавные на строчные, строчные на заглавные)"""
    
    text = input("Введите строку: ")
    result = ""

    for letter in text:
        if letter == 'а':
            current = 'б'
        elif letter == 'б':
            current = 'а'
        elif letter == 'А':
            current = 'Б'
        elif letter == 'Б':
            current = 'А'
        else:
            current = letter 

        if current.isupper():
            result += current.lower()
        elif current.islower():
            result += current.upper()
        else:
            result += current 

    print("Результат:", result)
