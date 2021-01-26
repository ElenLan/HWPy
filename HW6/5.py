# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title
# (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен
# выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод
# для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print('пишет синим')


class Pencil(Stationery):
    def draw(self):
        print("мягкий")


class Handle(Stationery):
    def draw(self):
        print("подчёркивает жёлтым")


stationery = Stationery('название')
stationery.draw()
pen = Pen('pilot')
print(pen.title)
pen.draw()
pencil = Pencil('koh-i-noor')
print(pencil.title)
pencil.draw()
handle = Handle('centropen')
print(handle.title)
handle.draw()
