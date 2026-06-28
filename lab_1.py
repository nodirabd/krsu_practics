#done
name = input("Ваши фамилия, имя? ")
age = int(input("Сколько Вам лет? "))
address = input("Где вы живете? ")

print(f"Ваши фамилия, имя: {name}\nВаш возраст: {age}\nВы живете в: {address}")
print(
    f"Ваши фамилия, имя: {name}",
    f"Ваш возраст: {age}",
    f"Вы живете в: {address}",
    sep="***"
)