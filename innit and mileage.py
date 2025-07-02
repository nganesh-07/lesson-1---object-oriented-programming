class vehicle:
    def __init__ (self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelX = vehicle(250, 20)

print("modelX's max speed:", modelX.max_speed)
print("modelX's mileage:", modelX.mileage)