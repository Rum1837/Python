import random
print("добро пожаловать в игру камень ножницы бумага!")
playerScore=0
botScore=0

raunds = int(input("Сколько раундов хотите сыграть?\n"))

for i in range(raunds):
    print(f"\n Счет игрока {playerScore} --- Счет бота {botScore} \n")
    answer = input("Что выберешь?\n").lower()
    if answer == "1": 
        answer = "камень"
    if answer == "2": 
       answer = "ножницы"
    if answer == "3": 
       answer = "бумага"
    if answer == "4": 
       answer = "ящерица"
    if answer == "5": 
        answer = "спок"

    if answer.find("камень") != -1:
        answer = "к"
    elif answer.find("ножницы") != -1:
        answer = "н"
    elif answer.find("бумага") != -1 or answer.find("бумагу") != -1:
        answer = "б"
    elif answer.find("ящерица") != -1:
        answer = "я"
    elif answer.find("спок") != -1:
        answer = "с"
    botAnswer = random.choice(["камень", "ножницы", "бумагу","ящерица","спок"])
    print(f"А я выберу {botAnswer}")
    botAnswer = botAnswer[0]
    print(botAnswer)
    if answer == botAnswer:
        print("ничья!")
    elif(answer == "к" and botAnswer == "н") or\
        (answer == "к" and botAnswer == "я") or \
        (answer == "н" and botAnswer == "я")or \
        (answer == "н" and botAnswer == "б") or \
        (answer == "я" and botAnswer == "б")or \
        (answer == "я" and botAnswer == "с") or \
        (answer == "б" and botAnswer == "к")or \
        (answer == "б" and botAnswer == "с") or \
        (answer == "с" and botAnswer == "к")or \
        (answer == "с" and botAnswer == "н"):
        print("Игрок победил!")
        playerScore+=1
    else:
        print("я победил!")
        botScore+=1

print(f"\n Счет игрока {playerScore} --- Счет бота {botScore} \n")
if playerScore == botScore:
    print(f"ничья по итогам {raunds} раундов!")
elif playerScore > botScore:
    print(f"ты победил по итогам {raunds} раундов")
else: print(f"Я победил по итогам {raunds} раундов")