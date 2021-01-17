# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

data = input('введите число - ')
num1 = int(data)
num2 = int(data + data)
num3 = int(data + data + data)

print(num1 + num2 + num3)

