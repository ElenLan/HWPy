# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: towncar, SportCar, workcar,
# PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов towncar и workcar переопределите метод show_speed. При значении скорости
# свыше 60 (towncar) и 40 (workcar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Выполните вызов методов и также покажите результат.
from time import sleep


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехали')

    def stop(self):
        print(f'{self.name} приехали')

    def turn_left(self):
        print(f'{self.name} повернули налево')

    def turn_right(self):
        print(f'{self.name} повернули направо')

    def show_speed(self):
        print(f'{self.name} скорость авто {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"{self.name} нас не догонят!")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} пицца остывает!!!')


towncar = TownCar(70, 'red', 'prius', False)
sportcar = Car(120, 'black', 'K.I.T.T.', False)
workcar = WorkCar(60, 'blue', 'ЯндексЕда', False)
policecar = Car(150, 'wight-black', 'officer', True)
towncar.go()
towncar.show_speed()
sleep(1)
sportcar.go()
sportcar.show_speed()
sleep(1)
workcar.go()
workcar.show_speed()
sleep(2)
towncar.turn_right()
print(f'{towncar.name} БЛИН, полиция!')
sleep(1)
print(f'{towncar.name} снизил до 40')
sleep(1)
sportcar.turn_left()
print(f'{sportcar.name} скорость 280')
print(f'{sportcar.name} не догонишь!')
sleep(1)
print(f'{policecar.name} не очень то и хотелось..')
sleep(1)
policecar.go()
policecar.show_speed()
sleep(2)
print(f'{policecar.name} прижмись вправо!')
sleep(1)
print(f'{workcar.name} да ёклмн :( ')
sleep(2)
workcar.stop()
policecar.stop()
sleep(2)
print(f'{policecar.name} документики')
sleep(1)
print(f'{workcar.name} да вы офигели!')
# понравилась версия Шамиля :)
