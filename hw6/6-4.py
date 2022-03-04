# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.


class Car:

    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Go')

    def stop (self, speed):
        print('Stop')

    def turn(self, direction):
        print(f'Car turned to {direction}')

    def show_speed(self):
        print(f'Current speed is {self.speed}')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'Внимание! Превышение скорости {self.speed} км/ч')

class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'Внимание! Превышение скорости {self.speed} км/ч')

class PoliceCar (Car):
    def __init__(self,speed, color, name):
        super().__init__(speed, color, name, True)

town = TownCar (70, 'red', 'Sport')
sport = SportCar (100, 'yellow', 'Sport')
work = WorkCar (35, 'green', 'Work')
police = PoliceCar (90, 'black', 'Police')

town.show_speed()
work.show_speed()

town.show_speed = 30
work.show_speed()

police.turn('left')


