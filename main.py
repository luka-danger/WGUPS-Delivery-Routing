from hashmap import HashMap
from package import Package
import csv 

# Read Address CSV file
# Attribution: https://docs.python.org/3/library/csv.html
with open("csv-files/addressCSV.csv") as addressCSV:
    ReadAddress = list(csv.reader(addressCSV))

with open("csv-files/distanceCSV.csv") as distanceCSV:
    ReadDistance = list(csv.reader(distanceCSV))


def load_package_data(csv_file, hash_map):
    with open(csv_file) as packageCSV:
        ReadPackage = list(csv.reader(packageCSV))
        # hash_map = HashMap()

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

package_hashmap = HashMap()

load_package_data("csv-files/packageCSV.csv", package_hashmap)

print(package_hashmap.lookup(3))
print(package_hashmap.lookup(40))

            