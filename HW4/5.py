# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
from functools import reduce


def my_res(num1, num2):
    return num1 * num2


my_list = [el for el in range(100, 1001)]

print(reduce(my_res, my_list))


