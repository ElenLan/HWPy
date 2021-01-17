# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month = int(input('введите номер месяца - '))
season = ['Зима', 'Весна', 'Лето', 'Осень']
weather = {'heat': 'Теплое время года', 'cold': 'Холодное время года'}
while month < 13:

    if month == 12 or month == 1 or month == 2:
        print((season[0]), (weather['cold']))
    elif month == 3 or month == 4 or month == 5:
        print((season[1]), (weather['heat']))
    elif month == 6 or month == 7 or month == 8:
        print((season[2]), (weather['heat']))
    elif month == 9 or month == 10 or month == 11:
        print((season[3]), (weather['cold']))
    else:
        print('error')
    break
