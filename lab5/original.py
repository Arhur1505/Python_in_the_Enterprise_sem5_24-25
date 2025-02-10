import random
import time
from multiprocessing import Process

class Car:
    def __init__(self, wheel_angle, speed):
        self.wheel_angle = wheel_angle
        self.speed = speed

    def set_speed(self, speed):
        self.speed = max(0, speed) 

    def turn(self, angle):
        self.wheel_angle += angle  

    def brake(self):
        self.speed = max(0, self.speed - 10) 

    def accelerate(self, amount):
        self.set_speed(self.speed + amount) 

    def __str__(self):
        return f"Wheel angle: {self.wheel_angle:.0f}, Speed: {self.speed:.0f}"

class Event:
    def __init__(self, car):
        self.car = car

    def crush(self):
        self.car.set_speed(10)
        self.car.turn(random.gauss(-30, 30))
        return 'crush'

    def limit_change(self):
        self.car.set_speed(random.gauss(30, 70))
        return 'limit_change'

    def police_officer(self):
        self.car.set_speed(self.car.speed + 40)
        self.car.turn(0)
        return 'police_officer'

    def obstacle(self):
        self.car.turn(random.gauss(-30, 30))
        self.car.brake()
        return 'obstacle'

    def clear_road(self):
        self.car.accelerate(10)
        self.car.turn(0)
        return 'clear_road'

    def show_car_status(self):
        return str(self.car)

class Environment:
    def __init__(self, car):
        self.car = car
        self.event_handler = Event(car)

    def random_event(self):
        events = [
            self.event_handler.crush,
            self.event_handler.limit_change,
            self.event_handler.police_officer,
            self.event_handler.obstacle,
            self.event_handler.clear_road
        ]
        return random.choice(events)()

    def run_simulation(self):
        print(f"Initial state: {self.car}")
        while True:
            event = self.random_event()
            print(f"Event: {event}")
            print(self.event_handler.show_car_status())
            time.sleep(1)

    def start_simulation(self):
        simulation_process = Process(target=self.run_simulation)
        simulation_process.start()
        return simulation_process

if __name__ == "__main__":
    car1 = Car(0, 40)
    environment = Environment(car1)

    environment.start_simulation()