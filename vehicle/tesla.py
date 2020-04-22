from .vehicle import Vehicle

class Tesla(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        self.battery_kwh = 0

    # def charge_battery(self):
    #     ... 