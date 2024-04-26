import random
timeList =["Сегодня", "Завтра", "Очень скоро"]
eventList = ["вы встретите", "с вами случится", "вы найдёте"]
objectList = ["что-то волшебное", "необычный инцидент", "большой сюрприз"]
zodiaki = ["Овен","Телец","БлизнецыРак","Лев","Дева","Весы","Скорпион","Стрелец","Козерог","Водолей","Рыбы"]         
while True:
    zodiak = input("введите знак Зодиака\n")
    if zodiak in zodiaki:
        time = timeList[random.randint(0, len(timeList) - 1)]
        event = eventList[random.randint(0, len(eventList) - 1)]
        object = objectList[random.randint(0, len(objectList) -1)]
        print(time + " " + event + " " + object)
        next = input("хотите попробовать ещё раз?\n")
        if next.lower() != "да" or next.lower() != "yes":
            break
    else:
        print("Такого нэту!")
print("Приходите ещё за новыми предсказаниями!")