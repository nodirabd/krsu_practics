import matplotlib.pyplot as plotlib

plotlib.rcParams['font.family'] = 'DejaVu Sans'
plotlib.rcParams['axes.unicode_minus'] = False

with open("data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

fio = lines[0].split()[1:]
oklad = list(map(float, lines[1].split()[1:]))
vydacha = list(map(float, lines[2].split()[1:]))

fio_labels = [name.replace('_', ' ') for name in fio]


plotlib.figure(figsize=(10, 7))
plotlib.pie(
    oklad, 
    labels=fio_labels, 
    autopct='%1.1f%%', 
    startangle=140, 
    shadow=False
)
plotlib.title('Распределение окладов по сотрудникам')
plotlib.tight_layout()
plotlib.show()


plotlib.figure(figsize=(12, 6))

x_positions = list(range(1, len(fio) + 1))
width = 0.35

plotlib.bar([x - width/2 for x in x_positions], oklad, width=width, color='royalblue', label='Оклад')
plotlib.bar([x + width/2 for x in x_positions], vydacha, width=width, color='crimson', label='Сумма к выдаче')

plotlib.title('Сравнение оклада и суммы к выдаче')
plotlib.xlabel('Сотрудники')
plotlib.ylabel('Рубли')
plotlib.xticks(x_positions, fio_labels, rotation=45)
plotlib.legend()
plotlib.tight_layout()
plotlib.show()