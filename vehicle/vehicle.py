class Vehicle:
    def __init__(self):
        self.main_color = ""
        self.maximum_occupancy = ""
        self.wheels = ""
        self.model = ""
        self.driving = False
        self.direction = ""

    def drive(self):
        self.driving = True
        return f'The {self.main_color} {self.model} roars past, pudder pudder putt'

    def turn(self, direction):
        if self.driving is True:
            self.direction = direction
        else:
            return 'cant turn a stopped car'

    def stop(self):
        if self.driving is True:
            self.driving = False
            print(f'The {self.main_color} {self.model} rolls to a stop in front of your moms house')
        