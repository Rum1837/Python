rightCounter = 0
questionsCounter = 0
questions = ["сколько цветов у радуги?", "какой языкмы изучаем?","По каким дням у нас ТРПО?","Какого цвета солнце?","Как меня зовут?"]
rightAnswers = ["7", "python","суббота","желтого","рома"]
while questionsCounter < len(questions):
    answer = input(questions[questionsCounter]+"\n")
    if answer.lower() == rightAnswers[questionsCounter]:
        rightCounter += 1
        print("Вы ответили верно\n------------------")
    else:
        print("Вы ответили не верно")
    questionsCounter += 1
print(f"вы набрали баллов: {rightCounter}")