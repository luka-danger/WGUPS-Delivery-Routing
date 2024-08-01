class Truck:
    def __init__(self, truck_id, capacity, speed, current_location, packages, mileage, departure):
        self.truck_id = truck_id
        self.capacity = capacity
        self.speed = speed
        self.current_location = current_location
        self.packages = packages
        self.mileage = mileage
        self.departure = departure


    def __str__(self):
        return f'{self.capacity}, {self.speed}, {self.current_location}, {self.packages},\
            {self.mileage}, {self.departure}'