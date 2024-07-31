from hashmap import HashMap
from package import Package
from truck import Truck
import csv 
import datetime

# Read Address CSV file
# Attribution: https://docs.python.org/3/library/csv.html


'''
Load Package Data Function 

Params: 
csv_file - CSV file containing relevant package details 
hash_map - HashMap where package data will be passed to

Iterates through each row of package data, indexes rows, and puts into a hashmap 
Key: Package ID (package_id)
Value: Package Info (address, city, state, zip_code, deadline, weight, special_notes)

Attribution: https://www.youtube.com/watch?v=efSjcrp87OY
'''
def load_package_data(csv_file, hash_map):
    # Read CSV Package File
    # Attribution: https://docs.python.org/3/library/csv.html
    with open(csv_file) as packageCSV:
        ReadPackage = list(csv.reader(packageCSV))

        # Iterate through each row in Package CSV and index row
        for row in ReadPackage:
            package_id = row[0]
            address = row[1]
            city = row[2]
            state = row[3]
            zip_code = row[4]
            deadline = row[5]
            weight = row[6]
            special_notes = row[7]

            # HashMap instance 
            # Value for HashMap
            package_data = Package(package_id, address, city, state, zip_code, deadline, weight, special_notes)
            
            # Use HashMap insert 
            # {Key: package_id, Value: Package_Data)
            hash_map.insert(package_id, package_data)
        print(hash_map)

# Instantiate HashMap
package_hashmap = HashMap()

# Load packages from CSV onto instantiated HashMap
load_package_data("csv-files/packageCSV.csv", package_hashmap)

# Store distance data points in empty array
distance_data = []

def load_distance_data():
    # Read CSV Distance File
    # Attribution: https://docs.python.org/3/library/csv.html
    with open("csv-files/distanceCSV.csv") as distanceCSV:
        ReadDistance = list(csv.reader(distanceCSV))

    # Iterate through each row in Distance CSV
    for distance in ReadDistance:
        # Append to distance_data array 
        distance_data.append(distance)

# Pass Distance CSV File to load_distance_data function
load_distance_data()

address_data = []

def load_address_data():
    # Read CSV Address file 
    # Attribution: https://docs.python.org/3/library/csv.html
    with open("csv-files/addressCSV.csv") as addressCSV:
        ReadAddress = list(csv.reader(addressCSV))

    # Iterate through each row of address
    for address in ReadAddress:
        # Append to address_data array
        address_data.append(address)


# Pass Address CSV File to load_address_data function
load_address_data()

# Look up items from address_data array
def lookup_address(index):
    # Ensure index is within the range of the list
    if 0 <= index < len(address_data):
        return address_data[index]
    else:
        return 'Index out of range'

print(lookup_address(26))

def distance_between(address1, address2):
    # Look at the distance between 2 addresses using indexes 
    try:
        address_distance = distance_data[address1][address2]
        if address_distance == '':
            address_distance = distance_data[address2][address1]
        return float(address_distance)
    # Prevent code from breaking if address not found
    except ValueError:
        return None
    # Prevent code from breaking if index out of range
    except IndexError: 
        return None

def min_distance(truck):
    # FIX ME 
    return None 

# Manually Load Trucks
# Instantiate Truck(id, capacity, speed, current location (WGU Hub), package array, mileage, departure time)
# Truck 1 leaves at 8:00am, the earliest it is allowed to leave the hub
truck_1 = Truck(1, 16, 18, '4001 South 700 East', [1, 4, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 26, 29, 31, 40], 0\
                , datetime.timedelta(hours=8, minutes=0, seconds=0))
# Truck 2 leaves at 9:10am, after delayed packages have arrived
truck_2 = Truck(2, 16, 18, '4001 South 700 East', [3, 5, 8, 18, 22, 30, 34, 36, 37, 38], 0\
                , datetime.timedelta(hours=9, minutes=10, seconds=0))
# Truck 3 leaves at 10:25am, after the correct destination for package 9 is known 
truck_3 = Truck(3, 16, 18, '4001 South 700 East', [2, 6, 7, 9, 10, 23, 24, 25, 27, 28, 32, 33, 35, 39], 0\
                , datetime.timedelta(hours=10, minutes=25, seconds=0))

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

