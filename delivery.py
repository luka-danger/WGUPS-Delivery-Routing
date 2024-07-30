from truck import Truck
from hashmap import HashMap
from distance import *

# Atribution: WGU C950 Instruction Doc
def nearest_neighbor(truck):
    while len(truck.packages) > 0:
        min_distance = 2000
        closest_package = None

        for packageID in truck.packages:
            package = HashMap.lookup(packageID)
            truck_location = truck.location 
            package_address = package.address
            distance = distance_between(truck_location, package_address)

            if distance < min_distance:
                min_distance = distance
                closest_package = package

        truck.mileage += min_distance

        truck.current_time += (min_distance / Truck.speed)

        closest_package.delivery_time = truck.currentTime

        closest_package.delivery_status = 'DELIVERED'