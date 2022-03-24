a = input('Введите номер месяца')
a = int(a)

if a > 0 and a < 13:
    if a > 2 and a < 6:
        print('Весна')
    elif a > 5 and a < 9:
        print('Лето')
    elif  a > 8 and a < 12:
        print('Осень')
    else:
        print('Зима')
else:
    print('Ошибка')
