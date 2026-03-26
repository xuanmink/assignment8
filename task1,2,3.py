class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom
    def floor_up(self):
        if self.current < self.top:
            self.current = self.current + 1
        print("Elevator floor:", self.current)
    def floor_down(self):
        if self.current > self.bottom:
            self.current = self.current - 1
        print("Elevator floor:", self.current)
    def go_to_floor(self, floor):
        while self.current < floor:
            self.floor_up()
        while self.current > floor:
            self.floor_down()
class Building:
    def __init__(self,bottom,top,num):
        self.bottom=bottom
        self.top=top
        self.elevators = []
        for i in range(num):
            self.elevators.append(Elevator(bottom, top))
    def run_elevator(self, num, floor):
        print("Elevator", num, "moving")
        self.elevators[num-1].go_to_floor(floor)
    def fire_alarm(self):
        print("FIRE ALARM")
        for i in range(len(self.elevators)):
            self.run_elevator(i+1, self.bottom)
b = Building(1,10,3)
b.run_elevator(1,5)
b.run_elevator(2,3)
b.fire_alarm()