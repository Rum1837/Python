price = 250
print("Введите кол-во конфет(масса в граммах)")
mass = int(input("Ввод массы: "))
if mass > 2000:
    mass /= 1000
    price = 200
    result = price * mass
elif mass <= 2000:
    mass /= 1000
    result = price * mass
print(f"Цена за килограмм: {price} рублей")
print(f"Масса конфет: {mass} кг")
print(f"Конечная цена: {result} рублей")