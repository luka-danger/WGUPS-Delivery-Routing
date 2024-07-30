class Truck:
    def __init__(self, capacity, speed, currentLocation, packages, mileage):
        self.capacity = capacity
        self.speed = speed
        self.currentLocation = currentLocation
        self.packages = packages
        self.mileage = mileage

    def __str__(self):
        return f'{self.capacity}, {self.speed}, {self.currentLocation}, {self.packages},
        {self.mileage}'