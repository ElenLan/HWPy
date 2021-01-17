# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

income = int(input('Введите выручку - '))
spend = int(input('Введите издержки - '))
profit = income - spend
if income > spend:
    print('Фирма работает с прибылью')
    profitability = profit / income
    print('Рентабельность: ' + str(profitability))
else:
    print('Фирма работает в убыток')

staff = int(input('Введите численность сотрудников - '))
print('Прибыль на одного сотрудника равна: ' + str((profit / staff)))
