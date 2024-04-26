import random

print("Введите длину пароля")
length = int(input("Ввод длины: "))
range_start= 10**(length-1)
range_end = (10**length)-1

print (f"Пароль {random.randint(range_start,range_end)}")
