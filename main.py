from logo import *
from hashmap import *
from package import *
from truck import *
from menu import *
from datetime import *
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
            departure = row[8] if len(row) > 8 else datetime.timedelta(hours=8, minutes=0)
            status = row[9] if len(row) > 9 else 'At Hub'
            delivery_time = row[10] if len(row) > 10 else 'NOT DELIVERED'
            truck_num = row[11] if len(row) > 11 else 0
        
            # HashMap instance 
            # Value for HashMap
            package_data = Package(package_id, address, city, state, zip_code, deadline, weight, special_notes, departure, status, delivery_time, truck_num)
            
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

'''
Load Package Data Function 

Params: 
address1 (current address), address2 (next address)

Calculates the distance between two address points. 
If no distance exists, find address from next address to current address.

Try-Except Prevents code from breaking when address is not found or out of range
'''
def distance_between(address1, address2):
    try:
        # Calculate distance between two addresses using index from address data array
        index_1 = address_data.index(address1)
        index_2 = address_data.index(address2)
        address_distance = distance_data[index_1][index_2]
        # If no distance listed, calculate address from next location to current location 
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

def assign_truck_num(truck):
    for package in truck.packages:
        package = package_hashmap.lookup(package)
        package.truck_num = truck.truck_id 
        package.departure = truck.departure 

assign_truck_num(truck_1)
assign_truck_num(truck_2)
assign_truck_num(truck_3)


'''
Nearest Neighbor Algorithm 

Params: 
Truck (1, 2, or 3)

Starting: Set the truck location to the hub. Instantiate an empty array for deliveries. 
(Used for a separate function)

Algorithm: Run while there are packages on truck and set the minimum distance to an infinite number.
Iterate through each package on the truck, using the hashmap lookup to find the package by ID. Use the 
distance between function to calculate the distance from the truck current location (starting at hub) and 
the truck location. The first distance will become the new min_distance and the current package will be the 
closest package. Iterate through each package until the shortest distance is found. 

Add the distance to the truck mileage and calculate the time based on distance / speed. Deliver the package, 
set the truck's new location, remove the package from the truck, and repeat the algorithm.

Edge Cases: 
Case 1 - Package 6 arrives late and has an earlier delivery time, so it is prioritized over other packages
on that truck. 

Case 2 - Packages 13, 14, 15, 19, and 20 should be delivered together.

Return - deliveres array 
(Contains each package details that can be used in other functions)

Attribution: WGU Resources (Example Nearest Neighbor Algorithm)
'''
def deliver_package(truck):
    truck.current_time = truck.departure 
    deliveries = []

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
                package.special_notes = 'Address Changed from 300 State St to 410 S State St'

            if package_id == 6:
                package = package_hashmap.lookup(6)
                closest_package = package
                closest_package_id = package_id
                deliveries.append(closest_package)

            elif distance < min_distance:
                min_distance = distance
                closest_package = package
                closest_package_id = package_id
                deliveries.append(closest_package)
                

        truck.mileage += min_distance

        travel_time = (min_distance / truck.speed)
        travel_time_converted = datetime.timedelta(hours=travel_time)

        truck.current_time += travel_time_converted
        closest_package.delivery_time = truck.current_time

        if closest_package.id == '14':
            ## ALSO DELIVER AND REMOVE packages 13, 15, 19, and 20 when 14 is delivered
            additional_packages = [13, 15, 19, 20]
            for package_id in additional_packages:
                if package_id in truck.packages:
                    package = package_hashmap.lookup(package_id)
                    package.delivery_time = truck.current_time
                    truck.packages.remove(package_id)
                    deliveries.append(package)
            
        truck.current_location = closest_package.address
        if closest_package_id in truck.packages:
            truck.packages.remove(closest_package_id)
        else:
            print(f"Package ID {closest_package_id} not found in truck.packages")   

    return deliveries 

def combine():
    all_deliveries = []
    delivery_1 = deliver_package(truck_1)
    for package in delivery_1:
        if package not in all_deliveries:
            all_deliveries.append(package)

    delivery_2 = deliver_package(truck_2)
    for package in delivery_2:
        if package not in all_deliveries:
            all_deliveries.append(package)

    delivery_3 = deliver_package(truck_3)
    for package in delivery_3:
        if package not in all_deliveries:
            all_deliveries.append(package)
    
    all_deliveries.sort(key=lambda pkg: pkg.delivery_time)

    return all_deliveries

def total_mileage():
    combine()

    total_mileage = truck_1.mileage + truck_2.mileage + truck_3.mileage
    print('\n')
    print(f'All packages delivered in {total_mileage} miles.')

def main_menu():
    print(logo)
    all_deliveries = combine()
    while True:
        print(menu)
        user_input = int(input("Choose an option: 1, 2, 3, 4, or 5?: \n"))

        if user_input == 1:
            total_mileage()

        elif user_input == 2:
            for package in all_deliveries:
                print(f'Package {package.id} delivered at {package.delivery_time}\n')
            total_mileage()

        elif user_input == 3:
            from datetime import datetime

            choose_package_id = int(input("Enter a Package ID to lookup: \n"))

            def timedelta_to_time(td):
                total_seconds = int(td.total_seconds())
                hours, remainder = divmod(total_seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                return datetime.time(datetime(1900, 1, 1, hours, minutes, seconds))

            try: 
                input_time = input("Enter current time in hh:mm:ss format:\n")
                current_time = datetime.strptime(input_time, "%H:%M:%S").time()

                selected_package = package_hashmap.lookup(choose_package_id)

                # Convert the delivery time from timedelta to time
                delivery_time_as_time = timedelta_to_time(selected_package.delivery_time)

                # Convert departure time from timedelta to time
                departure_time_as_time = timedelta_to_time(selected_package.departure)

                if current_time >= delivery_time_as_time:
                    selected_package.status = 'Delivered'
                    print(f'Package {selected_package.id} was delivered at {delivery_time_as_time}.\n')
                    print(f'Status: {selected_package.status}\n')
                elif current_time <= delivery_time_as_time and current_time < departure_time_as_time:
                    selected_package.status = 'At Hub'
                    print(f'Package {selected_package.id} has not been delivered yet. The delivery deadline is {selected_package.deadline}\n')
                    print(f'Status: {selected_package.status}, Scheduled Departure: {selected_package.departure}\n')
                elif current_time <= delivery_time_as_time and current_time > departure_time_as_time: 
                    selected_package.status = 'En Route'
                    print(f'Package {selected_package.id} has not been delivered yet. The delivery deadline is {selected_package.deadline}\n')
                    print(f'Status: {selected_package.status}, Departed At: {selected_package.departure}\n')
            
            except:
                print('Please enter valid time format (hh:mm:ss)')

        elif user_input == 4:
            from datetime import datetime

            def timedelta_to_time(td):
                total_seconds = int(td.total_seconds())
                hours, remainder = divmod(total_seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                return datetime.time(datetime(1900, 1, 1, hours, minutes, seconds))

            try: 
                input_time = input("Enter current time in hh:mm:ss format:\n")
                current_time = datetime.strptime(input_time, "%H:%M:%S").time()

                for package in all_deliveries:
                    # Convert the delivery time from timedelta to time
                    delivery_time_as_time = timedelta_to_time(package.delivery_time)

                    # Convert the delivery time from timedelta to time
                    departure_time_as_time = timedelta_to_time(package.departure)

                    if current_time >= delivery_time_as_time:
                        package.status = 'Delivered'
                        print(f'Package {package.id} was delivered at {delivery_time_as_time}.')
                        print(f'Status: {package.status}\n')
                    elif current_time <= delivery_time_as_time and current_time < departure_time_as_time:
                        package.status = 'At Hub'
                        print(f'Package {package.id} has not been delivered yet. The delivery deadline is {package.deadline}')
                        print(f'Status: {package.status}, Scheduled Departure: {package.departure}\n')
                    elif current_time <= delivery_time_as_time and current_time > departure_time_as_time: 
                        package.status = 'En Route'
                        print(f'Package {package.id} has not been delivered yet. The delivery deadline is {package.deadline}')
                        print(f'Status: {package.status}, Departed At: {package.departure}\n')

            except:
                print('Please enter valid time format (hh:mm:ss)')
            

        elif user_input == 5: 
            print('\n')
            print("Exiting Program\n")
            break
        
        else: 
            print('\n')
            print(f'{user_input} is an invalid input.\n')

main_menu()


