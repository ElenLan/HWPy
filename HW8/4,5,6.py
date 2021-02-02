# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.
# ----------
# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
# других данных, можно использовать любую подходящую структуру, например словарь.
# ---------
#  Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
# указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных
# на уроках по ООП.

class Storage:
    def __init__(self):
        pass


class Equipment:
    def __init__(self, name: str, price: int, series: int):
        self.name = name
        self.price = price
        self.series = series

    def __str__(self):
        return f'Название: {self.name} Цена: {self.price} Серия: {self.series}'


class Printer(Equipment):
    def __init__(self, name: str, price: int, series: int, use: str):
        self.use = use
        Equipment.__init__(self, name, price, series)

    def __str__(self):
        return f'Название: {self.name} Цена: {self.price} Серия: {self.series}\n Назначение: {self.use}'


class Scanner(Equipment):
    def __init__(self, name: str, price: int, series: int, use: str):
        self.use = use
        Equipment.__init__(self, name, price, series)

    def __str__(self):
        return f'Название: {self.name} Цена: {self.price} Серия: {self.series}\n Назначение: {self.use}'


class Xerox(Equipment):
    def __init__(self, name: str, price: int, series: int, use: str):
        self.use = use
        Equipment.__init__(self, name, price, series)

    def __str__(self):
        return f'Название: {self.name} Цена: {self.price} Серия: {self.series}\n Назначение: {self.use}'


equipment = Equipment('Genius', 500, 887)
print(equipment)
printer = Printer('HP', 12000, 342, 'print')
scanner = Scanner('Acer', 11000, 544, 'scanning')
xerox = Xerox('LG', 34000, 9354, 'copying')
print(printer)
print(scanner)
print(xerox)
