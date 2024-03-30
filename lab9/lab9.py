studentList = ["Вася", "Петя"]
markList = ["5","3"]
while True:
    answer = int(input("выберите действие\n"
                        "1-добавить студента\n"
                        "2-удалить студента по номеру\n"
                        "3-удалить студента по имени\n"
                        "4-посмотреть весь список студентов\n"
                        "5-посмотреть оценку студента\n"
                        "0-выйти из программы\n"))
    if answer not in [1, 2 , 3, 4, 5, 0]:
        print("такой команды нет")
        continue
    elif answer == 1:
         newStudent = input("введите имя студента\n")
         studentList.append(newStudent)
    elif answer == 2:
        delStudent = int(input("введите номер студентадля удаления\n"))
    elif answer == 3:
        delNumber = input("введите имя студента для удаления\n")
        studentList.remove(delNumber)
    elif answer == 4:
        print(studentList)
    elif answer == 5:
        student = input("введите имя студента для просмотра его оценки\n")
        
    elif answer == 0:
        break