sum = 0
counter = 0
number = int(input("введите оценку от 1 до 12, 0 - прекратить ввод: "))
while number != 0:
 sum += number
 counter += 1
 number = int(input("введите оценку от 1 до 12, 0 - прекратить ввод: "))
print(sum/counter)