# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно
# обработать эту ситуацию и не завершиться с ошибкой.

class MyError(Exception):
    def __init__(self, text):
        self.text = text


class Divis:
    def __init__(self, dividend, divider):
        self.dividend = dividend
        self.divider = divider

    def division(self, dividend, divider):

        try:

            return (dividend // divider)
        except:
            return 'Деление на ноль'


divis = Divis(4, 2)
print(divis.division(60, 30))
print(divis.division(24, 6))
print(divis.division(4, 0))
