import random
class Car:
    def __init__(self, reg_num, max_spd):
        self.registration_number = reg_num
        self.maximum_speed = max_spd
        self.current_speed = 0
        self.travelled_distance = 0
    def accelerate(self, change):
        self.current_speed = self.current_speed + change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0
    def drive(self, hours):
        self.travelled_distance= self.travelled_distance + (self.current_speed * hours)
class Race:
    def __init__(self, name,distance,cars):
        self.name=name
        self.distance =distance
        self.cars =cars
    def hour_passes(self):
        for c in self.cars:
            c.accelerate(random.randint(-10,15))
            c.drive(1)
    def print_status(self):
        for c in self.cars:
            print(c.registration_number,c.maximum_speed,c.current_speed,c.travelled_distance)
    def race_finished(self):
        for c in self.cars:
            if c.travelled_distance >= self.distance:
                return True
        return False
cars_list=[]
for i in range(1, 11):
    cars_list.append(Car("ABC-" + str(i),random.randint(150, 200)))
my_race = Race("Grand Demolition Derby", 8000, cars_list)
hours = 0
while my_race.race_finished() == False:
    my_race.hour_passes()
    hours = hours + 1
    if hours % 10 == 0:
        print("Hours:", hours)
        my_race.print_status()
print("Final")
my_race.print_status()