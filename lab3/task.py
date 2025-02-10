import random
import time
import multiprocessing

class Car:
    def __init__(self, wheel_angle=0, speed=0):
        self.wheel_angle = wheel_angle
        self.speed = speed
        self.fuel_level = 100

    def accelerate(self):
        if self.fuel_level > 0:
            self.speed = min(150, self.speed + random.uniform(5, 20))
            self.consume_fuel()

    def brake(self):
        self.speed = max(0, self.speed - random.uniform(5, 20))

    def steer(self, angle):
        self.wheel_angle = max(-30, min(30, self.wheel_angle + angle))

    def refuel(self):
        self.fuel_level = 100

    def consume_fuel(self):
        self.fuel_level = max(0, self.fuel_level - (self.speed / 50))
        if self.fuel_level == 0:
            self.speed = 0

    def get_status(self):
        return f"wheel_angle: {self.wheel_angle:.2f}, speed: {self.speed:.2f}, fuel_level: {self.fuel_level:.2f}"

class Environment:
    def __init__(self):
        self.events = ['police', 'traffic', 'accident', 'fuel_station', None]

    def random_event(self):
        return random.choice(self.events)

    def generate_event_stream(self):
        while True:
            yield self.random_event()

    def wait(self, duration=1):
        time.sleep(duration)

    def time_of_day(self):
        return random.choice(['day', 'night'])

class Action:
    def __init__(self, car):
        self.car = car

    def respond_to_event(self, event):
        if event == 'accident':
            self.car.brake()
            return "Accident: car stopped"
        elif event == 'police':
            self.car.brake()
            return "Police nearby: slowing down"
        elif event == 'traffic':
            self.car.brake()
            return "Traffic detected: stopping"
        elif event == 'fuel_station':
            self.car.refuel()
            return "Fuel station: refueling"
        else:
            self.car.accelerate()
            return "Car is driving normally"

    def adjust_for_conditions(self, time_of_day):
        if time_of_day == 'night':
            self.car.brake()
            return "Driving at night: slowing down"
        return "Daytime driving: maintaining speed"

    def steer_randomly(self):
        angle = random.uniform(-5, 5)
        self.car.steer(angle)
        return f"Adjusting steering by {angle:.2f} degrees"

    def execute_action(self, event_stream, environment):
        for event in event_stream:
            msg_event = self.respond_to_event(event)
            msg_steer = self.steer_randomly()
            msg_conditions = self.adjust_for_conditions(environment.time_of_day())
            yield f"{msg_event} | {msg_steer} | {msg_conditions} | Status: {self.car.get_status()}"

def simulation_loop(action_handler, environment):
    for message in action_handler.execute_action(environment.generate_event_stream(), environment):
        print(message)
        environment.wait()

if __name__ == "__main__":
    car = Car()
    environment = Environment()
    action_handler = Action(car)

    sim_process = multiprocessing.Process(target=simulation_loop, args=(action_handler, environment))
    sim_process.start()

    input("Press Enter to end the simulation.\n")
    sim_process.terminate()