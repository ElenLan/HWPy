# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной
# платы сотрудника.В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

# while True:
#     num = input('для выхода - quit, продолжить - enter')
#     if num == 'quit':
#         break
#     else:
#         from module_hw4 import cash
#         print(cash())

from sys import argv


def cash():
    hours, payment, premium = argv
    print(hours * payment + premium)


cash()
#что-то я его не победила