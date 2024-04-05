studentList = ["Вася", "Петя"]
markList = ["5", "3"]
while True:
    answer = int(input("выберите действие\n"
                       "1-добавить студента\n"
                       "2-удалить студента по номеру\n"
                       "3-удалить студента по имени\n"
                       "4-посмотреть весь список студентов\n"
                       "5-посмотреть оценку студентов\n"
                        "6-посмотреть студента\n"
                       "0-выйти из программы\n"))
    if answer not in [1, 2, 3, 4, 5,6, 0]:
        print("такой команды нет")
        continue
    elif answer == 1:
        newStudent = input("введите имя студента\n")
        studentList.append(newStudent)
        newMark = input("введите оценку студента\n")
        markList.append(newMark)
    elif answer == 2:
        delStudent = int(input("введите номер студента для удаления\n"))
        if 0 <= delStudent < len(studentList):
            del studentList[delStudent]
            del markList[delStudent]
        else:
            print("Студент с таким номером не найден")
    elif answer == 3:
        delName = input("введите имя студента для удаления\n")
        if delName in studentList:
            index = studentList.index(delName)
            del studentList[index]
            del markList[index]
        else:
            print("Студент с таким именем не найден")
    elif answer == 4:
        print("Список студентов:", studentList)
    elif answer == 5:
        print("Студенты и их оценки:")
        for student, mark in zip(studentList, markList):
            print(f"{student}: {mark}")
    elif answer == 6:
        searchName = input("Введите имя студента для поиска\n")
        if searchName in studentList:
            index = studentList.index(searchName)
            print(f"{studentList[index]}: {markList[index]}")
        else:
            print("Студент с таким именем не найден")
    elif answer == 0:
        break
