from .vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        self.gallons_per_hour = 0

    # def charge_battery(self):
    #     ... 