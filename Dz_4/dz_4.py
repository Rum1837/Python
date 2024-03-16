ru = int(input("введите рубли "))
valuta = input("Введите валюту ")
dollar = 96
euro = 105
if(valuta == "Доллар" or valuta == "доллар"):
  res= ru/ dollar 
  print(res)
elif(valuta == "Евро" or valuta == "евро"):
  res= ru/euro
  print(res)