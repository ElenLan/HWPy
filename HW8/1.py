# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @ classmethod. Он должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число». Второй, с декоратором @ staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, day_info):
        self.day_info = day_info

    @classmethod
    def ext_num(cls, day_info):
        day_list = day_info.split('-')
        day = day_list[0]
        month = day_list[1]
        year = day_list[2]
        data = [day, month, year]
        return data

    @staticmethod
    def val_num(day, month, year):
        if day < 1 or day > 31:
            print('wrong day')
        elif month < 1 or month > 12:
            print('wrong month')
        elif year < 2021 or year > 2021:
            print('wrong year')
        else:
            print('OK')


date = Date('01-02-2021')
print(date.day_info)
print(date.ext_num('29-03-1988'))
Date.val_num(12, 4, 2312)
Date.val_num(15, 6, 2021)
