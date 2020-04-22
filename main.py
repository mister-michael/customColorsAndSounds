from vehicle import Tesla, Vehicle, Motorcycle

bob = Tesla()
bob.battery_kwh = 10
bob.main_color = "red"
bob.model = "SXF91"

dick = Motorcycle()
dick.gallons_per_hour = 4
dick.main_color = "white"
dick.model = "honda"

print(dick.drive())
dick.turn("north")
print(dick.stop())

print(bob.drive())
bob.turn("west")
print(bob.stop())

