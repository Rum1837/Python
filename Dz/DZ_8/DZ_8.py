answer = input("Введите предложение\n").lower()
inpud = input("Слово которое вы ищите\n")
if answer.find(inpud) != -1:
    poz = answer.find(inpud)
    print(poz+1)