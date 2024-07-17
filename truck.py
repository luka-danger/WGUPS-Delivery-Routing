class Truck:
    def __init__(self, capacity, currentLocation, packages, mileage):
        self.capacity = capacity
        self.currentLocation = currentLocation
        self.packages = packages
        self.mileage = mileage

    def __str__(self):
        return f'{self.capacity}, {self.currentLocation}, {self.packages},
        {self.mileage}'