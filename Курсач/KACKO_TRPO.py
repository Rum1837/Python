brand_tariffs = {
    "toyota": {"tariff": 0.03, "price": 2325000},
    "ford": {"tariff": 0.035, "price": 2470000},
    "bmw": {"tariff": 0.04, "price": 3720000},
    "mercedes-benz": {"tariff": 0.045, "price": 4192500},
    "audi": {"tariff": 0.042, "price": 3911500},
    "volkswagen": {"tariff": 0.038, "price": 3534000},
    "chevrolet": {"tariff": 0.037, "price": 3441000},
    "hyundai": {"tariff": 0.032, "price": 2976000},
    "kia": {"tariff": 0.033, "price": 3069000},
    "nissan": {"tariff": 0.036, "price": 3348000},
    "honda": {"tariff": 0.034, "price": 3159000},
    "subaru": {"tariff": 0.039, "price": 3627000},
    "mazda": {"tariff": 0.035, "price": 3222000},
    "lexus": {"tariff": 0.043, "price": 4929000},
    "volvo": {"tariff": 0.041, "price": 4833000},
    "porsche": {"tariff": 0.048, "price": 7776000},
    "jeep": {"tariff": 0.037, "price": 3441000},
    "land rover": {"tariff": 0.046, "price": 6099000},
    "mitsubishi": {"tariff": 0.034, "price": 3159000},
    "fiat": {"tariff": 0.031, "price": 2883000}
}

while True:
    choice = input("Введите '1' для расчета платежа по КАСКО, '2' для просмотра списка брендов или '0' для выхода: ")
    
    if choice == '1':
        car_brand = input("Введите марку автомобиля: ").lower()
        car_price = float(input("Введите цену автомобиля: "))
        if car_brand in brand_tariffs:
            tariff = brand_tariffs[car_brand]["tariff"]
            payment = car_price * tariff
            print("Платеж по КАСКО для {} составляет: {:.2f} рублей".format(car_brand.title(), payment))
        else:
            print("Бренд не найден в базе тарифов.")
    
    elif choice == '2':
        print("Доступные марки автомобилей со средней ценой:")
        for idx, (brand, details) in enumerate(brand_tariffs.items(), start=1):
            print("- {}: {:.2f} рублей (нажмите '{}' для расчета КАСКО)".format(brand.title(), details["price"], idx))

        brand_choice = input("Выберите номер марки для расчета КАСКО или введите '0' для выхода: ")
        if brand_choice.isdigit():
            brand_choice = int(brand_choice)
            if 1 <= brand_choice <= len(brand_tariffs):
                brand = list(brand_tariffs.keys())[brand_choice - 1]
                tariff = brand_tariffs[brand]["tariff"]
                car_price = brand_tariffs[brand]["price"]
                payment = car_price * tariff
                print("Платеж по КАСКО для {} составляет: {:.2f} рублей".format(brand.title(), payment))
            elif brand_choice == 0:
                print("Возвращение в основное меню...")
            else:
                print("Неверный выбор. Пожалуйста, введите номер марки из списка.")
        else:
            print("Неверный выбор. Пожалуйста, введите число.")

    
    
    elif choice == '0':
        print("Завершение программы...")
        break
    
    else:
        print("Неверный выбор. Пожалуйста, введите '1', '2' или '0'.")

