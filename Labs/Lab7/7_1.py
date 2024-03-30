import random

botNumber = random.randint(1, 10)
playerNumber = int(input("Введите число - "))

if playerNumber is None:
    print("Введи число")
else:
    while playerNumber != botNumber:
        if playerNumber > botNumber:
            print("Ты не угадал, моё число, оно меньше твоего")
        else:
            print("Ты не угадал, моё число, оно больше твоего")

        difference = playerNumber - botNumber
        if abs(difference) <= 2:
            print("Горячо")
        elif abs(difference) <= 4:
            print("Тепло")
        else:
            print("Холодно")

        playerNumber = int(input("Введите число - "))

    print(f"Ты угадал, моё число: {botNumber}")
