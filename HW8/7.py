# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса
# (комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.


class ComplexNumber:
    def __init__(self, real, imag=0):
        self.complex = complex(real, imag)

    def __add__(self, other):
        return other + self.complex

    def __mul__(self, other):
        return other * self.complex


a = ComplexNumber(7, 4)
b = ComplexNumber(13)
c = a + b
d = a * b
print(c)
print(d)
