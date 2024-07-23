from hashmap import HashMap
from package import Package
import csv 

# Read Address CSV file
# Attribution: https://docs.python.org/3/library/csv.html
with open("csv-files/addressCSV.csv") as addressCSV:
    ReadAddress = list(csv.reader(addressCSV))

with open("csv-files/distanceCSV.csv") as distanceCSV:
    ReadDistance = list(csv.reader(distanceCSV))

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
    with open(csv_file) as packageCSV:
        ReadPackage = list(csv.reader(packageCSV))

        for row in ReadPackage:
            package_id = row[0]
            address = row[1]
            city = row[2]
            state = row[3]
            zip_code = row[4]
            deadline = row[5]
            weight = row[6]
            special_notes = row[7]

            package_data = Package(package_id, address, city, state, zip_code, deadline, weight, special_notes)
            
            hash_map.insert(package_id, package_data)
        print(hash_map)

# Instantiate HashMap
package_hashmap = HashMap()

# Load packages from CSV onto instantiated HashMap
load_package_data("csv-files/packageCSV.csv", package_hashmap)

            