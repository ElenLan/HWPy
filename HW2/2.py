# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

a = []
a.insert(0, input('введите первый пункт - '))
a.insert(1, input('введите второй пункт - '))
a.insert(2, input('введите третий пункт - '))
a.insert(3, input('введите четвёртый пункт - '))
print(a)
n1, n2 = a[0], a[1]
n3, n4 = a[2], a[3]
n1, n2 = n2, n1
n3, n4 = n4, n3
print(n1, n2, n3, n4)
