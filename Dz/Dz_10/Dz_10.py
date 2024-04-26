import random

Questions = ["Какая сегодня погода?", "Чем займемся сегодня брейн?", "Когда?"]
Day = ["Сегодня прекрасная погода", "Сегодня ужасная погода", "Обычная"]
Brain = ["Сегодня Пинки, мы попытаемся захватить мир", "Сегодня не получилось захватить мир. Значит попробуем сделать завтра", "Оооо Пинки, сегондя мы снова попытаемся захватить мир!"]
Kogda = ["Потом", "Завтра", "Никогда"]

while True:
    for i in range(len(Questions)):
        print(f"Вопрос №{i+1}-{Questions[i]}")
    massivs = input("Задайте вопрос? Все вопросы перед вами\n")

    if massivs == "Какая сегодня погода?":
        day = Day[random.randint(0, len(Day) - 1)]
        print(day)
    elif massivs == "Чем займемся сегодня брейн?":
        mouse = Brain[random.randint(0, len(Brain) - 1)]
        print(mouse)
    elif massivs == "Когда?":
        never = Kogda[random.randint(0, len(Kogda) - 1)]
        print(never)

    next_answer = input("Хотите попробовать ещё раз?\n")
    if next_answer.lower() != "да" and next_answer.lower() != "yes":
        break

print("Приходите ещё!")
