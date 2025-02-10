import random
import sys

class Car:
    def __init__(self, wheel_angle = 0, speed = 0):
        self.wheel_angle = wheel_angle;
        self.speed = speed;

    def changeSpeed(self):
        self.speed = random.uniform(0, 150)

    def changeAngle(self):
        self.wheel_angle = random.uniform(-20, 20)

    def act(self, event):
        if event == 'wypadek':
            self.speed = 0;
            print('Lekka kraksa, koniec jazdy')
            sys.exit(0)
        if event == 'policja':
            self.speed = self.speed/2;
            print('Kierowco zwolnij')
        if event == 'korek':
            self.speed = 0;
            print('Stoimy w korku')

if __name__ == "__main__":
    event = ['policja', 'korek', 'wypadek']
    car1 = Car(0, 40)
    print(car1.wheel_angle, car1.speed)
    car1.act('policja')

    y = "tak";
    while y != "nie":
        y = input("Czy chcesz przeprowadzic symulacje? tak/nie: ")
        if y == "tak":
            x = input("Podaj ilosc przebiegu petli: ")
            n = 0
            while n < int(x):
                print('Kat, Predkosc')
                print(car1.wheel_angle, car1.speed)
                car1.changeAngle();
                car1.changeSpeed();
                n = n + 1