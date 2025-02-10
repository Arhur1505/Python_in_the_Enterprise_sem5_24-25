#path to my colleague's source code
#/home/stud2022/2starzyk/Documents/S5/Python/lab_02/task.py
import random
import time
from multiprocessing import Process
import unittest

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

class TestSimulation(unittest.TestCase):
    def setUp(self):
        self.car = Car(0, 40)
        self.event = Event(self.car)

    def test_set_speed(self):
        self.car.set_speed(50)
        self.assertEqual(self.car.speed, 50)
        self.car.set_speed(-10)
        self.assertEqual(self.car.speed, 0)

    def test_turn(self):
        self.car.turn(30)
        self.assertEqual(self.car.wheel_angle, 30)
        self.car.turn(-15)
        self.assertEqual(self.car.wheel_angle, 15)

    def test_brake(self):
        self.car.brake()
        self.assertEqual(self.car.speed, 30)
        self.car.brake()
        self.assertEqual(self.car.speed, 20)

    def test_accelerate(self):
        self.car.accelerate(20)
        self.assertEqual(self.car.speed, 60)
        self.car.accelerate(-10)
        self.assertEqual(self.car.speed, 50)

    def test_crush(self):
        result = self.event.crush()
        self.assertEqual(result, 'crush')
        self.assertEqual(self.car.speed, 10)

    def test_police_officer(self):
        result = self.event.police_officer()
        self.assertEqual(result, 'police_officer')
        self.assertEqual(self.car.speed, 80)

    def test_obstacle(self):
        result = self.event.obstacle()
        self.assertEqual(result, 'obstacle')
        self.assertLessEqual(self.car.speed, 30)

    def test_clear_road(self):
        result = self.event.clear_road()
        self.assertEqual(result, 'clear_road')
        self.assertEqual(self.car.speed, 50)

    def test_show_car_status(self):
        status = self.event.show_car_status()
        self.assertEqual(status, "Wheel angle: 0, Speed: 40")

    def test_car_string_representation(self):
        self.assertEqual(str(self.car), "Wheel angle: 0, Speed: 40")
        self.car.turn(15)
        self.car.accelerate(20)
        self.assertEqual(str(self.car), "Wheel angle: 15, Speed: 60")

if __name__ == "__main__":
    car1 = Car(0, 40)
    environment = Environment(car1)
    environment.start_simulation()

    unittest.main()