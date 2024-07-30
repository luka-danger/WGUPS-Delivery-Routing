from hashmap import HashMap
from package import Package
from truck import Truck
import csv 

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

def load_distance_data(csv_file):
    # Read CSV Distance File
    # Attribution: https://docs.python.org/3/library/csv.html
    with open(csv_file) as distanceCSV:
        ReadDistance = list(csv.reader(distanceCSV))

    # Iterate through each row in Distance CSV
    for distance in ReadDistance:
        # Append to distance_data array 
        distance_data.append(distance)

# Pass Distance CSV File to load_distance_data function
load_distance_data("csv-files/distanceCSV.csv")

addressData = []

def load_address_data(csv_file):
    # Read CSV Address file 
    # Attribution: https://docs.python.org/3/library/csv.html
    with open(csv_file) as addressCSV:
        ReadAddress = list(csv.reader(addressCSV))

    # Iterate through each row of address
    for address in ReadAddress:
        # Append to address_data array
        addressData.append(address)

# Pass Address CSV File to load_address_data function
load_address_data("csv-files/addressCSV.csv")

def distance_between(address1, address2):
    # FIX ME
    return distance_data[addressData.index(address1)][addressData.index(address2)]

# Manually Load Trucks
# Instantiate Truck(capacity, speed, current location (WGU Hub), package array, mileage)
truck_1 = Truck(16, 18, '4001 South 700 East', [1, 4, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 26, 29, 31, 40], 0)
truck_2 = Truck(16, 18, '4001 South 700 East', [3, 5, 8, 18, 22, 30, 34, 36, 37, 38], 0)
truck_3 = Truck(16, 18, '4001 South 700 East', [2, 6, 7, 9, 10, 23, 24, 25, 27, 28, 32, 33, 35, 39], 0)




