from logo import *
from hashmap import *
from package import *
from truck import *
from menu import *
import csv 
import datetime

print(logo)

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
            status = row[8] if len(row) > 8 else 'No Status'
            delivery_time = row[9] if len(row) > 9 else 'NOT DELIVERED'

            # HashMap instance 
            # Value for HashMap
            package_data = Package(package_id, address, city, state, zip_code, deadline, weight, special_notes, status, delivery_time)
            
            # Use HashMap insert 
            # {Key: package_id, Value: Package_Data)
            hash_map.insert(package_id, package_data)

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
        address_data.append(address[2])


# Pass Address CSV File to load_address_data function
load_address_data()

# Look up items from address_data array
def lookup_address(index):
    # Ensure index is within the range of the list
    if 0 <= index < len(address_data):
        return address_data[index]
    else:
        return 'Index out of range'
    

def distance_between(address1, address2):
    # Look at the distance between 2 addresses using indexes 
    try:
        index_1 = address_data.index(address1)
        index_2 = address_data.index(address2)
        address_distance = distance_data[index_1][index_2]
        # FIX ME: Move to load_distance_data 
        if address_distance == '':
            address_distance = distance_data[index_2][index_1]
        return float(address_distance)
    # Prevent code from breaking if address not found
    except ValueError:
        return None
    # Prevent code from breaking if index out of range
    except IndexError: 
        return None
    

# Manually Load Trucks
# Instantiate Truck(id, capacity, speed, current location (WGU Hub), package array, mileage, departure time)
# Truck 1 leaves at 8:00am, the earliest it is allowed to leave the hub
truck_1 = Truck(1, 16, 18, '4001 South 700 East', [1, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 29, 30, 31, 37, 40], 0\
                , datetime.timedelta(hours=8, minutes=0))
# Truck 2 leaves at 9:10am, after delayed packages have arrived
truck_2 = Truck(2, 16, 18, '4001 South 700 East', [3, 4, 6, 8, 18, 22, 25, 26, 34, 36, 38], 0\
                , datetime.timedelta(hours=9, minutes=10))
# Truck 3 leaves at 10:25am, after the correct destination for package 9 is known 
truck_3 = Truck(3, 16, 18, '4001 South 700 East', [2, 5, 7, 9, 10, 23, 24, 27, 28, 32, 33, 35, 39], 0\
                , datetime.timedelta(hours=10, minutes=25))


# Atribution: WGU C950 Instruction Doc
## FIX ME

def deliver_package(truck):
    truck.current_time = truck.departure 
    distance = []
    delivery_info = []

    while len(truck.packages) > 0:
        min_distance = float('inf')
        closest_package = None 

        for package_id in truck.packages: 
            package = package_hashmap.lookup(package_id)
            package_address = package.address 
            truck_location = truck.current_location 
            distance = distance_between(truck_location, package_address)
            
            if package_id == 9: 
                package = package_hashmap.lookup(9)
                package.address = '410 S State St'
                package.zip_code = '84111'

            if package_id == 6:
                package = package_hashmap.lookup(6)
                closest_package = package
                closest_package_id = package_id

            elif distance < min_distance:
                min_distance = distance
                closest_package = package
                closest_package_id = package_id
                

        truck.mileage += min_distance

        travel_time = (min_distance / truck.speed)
        travel_time_converted = datetime.timedelta(hours=travel_time)

        truck.current_time += travel_time_converted
        closest_package.delivery_time = truck.current_time
        closest_package.status = 'DELIVERED'
        delivery_info.append((closest_package.id, closest_package.delivery_time))
        print(f'Package {closest_package.id} delivered at {closest_package.delivery_time}')

        if closest_package.id == '14':
            ## ALSO DELIVER AND REMOVE packages 13, 15, 19, and 20 when 14 is delivered
            additional_packages = [13, 15, 19, 20]
            for package_id in additional_packages:
                if package_id in truck.packages:
                    package = package_hashmap.lookup(package_id)
                    package.delivery_time = truck.current_time
                    package.status = 'DELIVERED'
                    truck.packages.remove(package_id)
                    print(f'Package {package_id} also delivered at {package.delivery_time} with Package 14')
        
        truck.current_location = closest_package.address
        if closest_package_id in truck.packages:
            truck.packages.remove(closest_package_id)
        else:
            print(f"Package ID {closest_package_id} not found in truck.packages")

    return delivery_info
        
def print_all_info():
    deliver_package(truck_1)
    deliver_package(truck_2)
    deliver_package(truck_3)
 

def main_menu():

    print(menu)
    user_input = int(input("Choose an option: 1, 2, 3, or 4?: \n"))
    if user_input == 1:
        print_all_info()

        total_mileage = truck_1.mileage + truck_2.mileage + truck_3.mileage
        print('\n')
        print(f'All packages delivered in {total_mileage} miles.')
        print('\n')

    if user_input == 2:
        choose_package_id = int(input("Enter a Package ID to lookup: \n"))
        selected_package_id = package_hashmap.lookup(choose_package_id)
        print(selected_package_id)

        
        

        # choose_time_hour = int("Enter an hour: \n")
        # choose_time_minute = int("Enter a minute: \n")

main_menu()