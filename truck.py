class Truck:
    def __init__(self, truck_id, capacity, speed, currentLocation, packages, mileage, departure):
        self.truck_id = truck_id
        self.capacity = capacity
        self.speed = speed
        self.currentLocation = currentLocation
        self.packages = packages
        self.mileage = mileage
        self.departure = departure

    def __str__(self):
        return f'{self.capacity}, {self.speed}, {self.currentLocation}, {self.packages},\
            {self.mileage}, {self.departure}'