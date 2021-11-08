print("Задача 4")
# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула(куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        # каждый атрибут записываю в свой защищенный атрибут
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # определяю методы
    def go(self):
        print('{} is going!'.format(self.name))

    def stop(self):
        print('{} is stoping!'.format(self.name))

    def turn(self, direction):
        print('{} is turning to {}!'.format(self.name, direction))

    def show_speed(self):
        print('Current speed:', self.speed)

# переопределяю метод
class TownCar(Car):

    # обращаюсь к show_speed родительского класса
    def show_speed(self):
        # определяю то как он работает, с помощью super использую метод родителя
        super().show_speed()
        # добавляю его функционал
        if self.speed > 60:
            print('Warning! Your speed is more than max!')

# создаю класс SportCar без функционала
class SportCar(Car):
    pass


class WorkCar(Car):
    # полностью переопределяю класс
    def show_speed(self):
        # скопипастил из определения метода
        print('Current speed:', self.speed)
        # добавляю новый функционал
        if self.speed > 40:
            print('Warning! Your speed is more than max!')

# создаю класс SportCar без функционала
class PoliceCar(Car):
    pass

# передаю данные
sport_car = SportCar(220, 'Желтая', 'Спортивная машина', False)
town_car = TownCar(150, 'Белая', 'Городская машина', False)
work_car = WorkCar(70, 'Красная', 'Рабочая машина', False)
police_car = PoliceCar(180, 'Синяя', 'Полицейская машина', True)

# Вызываю методы и показываю результат.
sport_car.show_speed()
town_car.show_speed()
work_car.show_speed()
police_car.show_speed()
sport_car.turn('left')
