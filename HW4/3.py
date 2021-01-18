# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
# Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.

from random import randint
numbers = randint(20, 241)
my_list = [num for num in range(numbers) if num % 20 == 0 or num % 21 == 0]
print(my_list)

