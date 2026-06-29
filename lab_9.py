import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

with open("data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

fio = lines[0].split()[1:]
oklad = list(map(float, lines[1].split()[1:]))
vydacha = list(map(float, lines[2].split()[1:]))

fio_labels = [name.replace('_', ' ') for name in fio]


plt.figure(figsize=(10, 7))
plt.pie(
    oklad, 
    labels=fio_labels, 
    autopct='%1.1f%%', 
    startangle=140, 
    shadow=False
)
plt.title('Распределение окладов по сотрудникам')
plt.tight_layout()
plt.show()


plt.figure(figsize=(12, 6))

x_positions = list(range(1, len(fio) + 1))
width = 0.35

plt.bar([x - width/2 for x in x_positions], oklad, width=width, color='royalblue', label='Оклад')
plt.bar([x + width/2 for x in x_positions], vydacha, width=width, color='crimson', label='Сумма к выдаче')

plt.title('Сравнение оклада и суммы к выдаче')
plt.xlabel('Сотрудники')
plt.ylabel('Рубли')
plt.xticks(x_positions, fio_labels, rotation=45)
plt.legend()
plt.tight_layout()
plt.show()