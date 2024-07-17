import csv 

# Read Address CSV file
# Attribution: https://docs.python.org/3/library/csv.html
with open("csv-files/addressCSV.csv") as addressCSV:
    ReadAddress = list(csv.reader(addressCSV))

with open("csv-files/distanceCSV.csv") as distanceCSV:
    ReadDistance = list(csv.reader(distanceCSV))

with open("csv-files/packageCSV.csv") as packageCSV: 
    ReadPackage = list(csv.reader(packageCSV))

# Attribution: WGU Webinar 1: "Let's Go Hashing"
class HashMap:
    # Create 10 bucket hash table 
    def __init__(self, initial_size = 10):
        # Create empty buckets
        self.hashlist = []
        # Append empty buckets to a list
        for i in range(initial_size):
            self.hashlist.append([])

    def insert(self, key, value):
        # Hash Function: Assign each item to a bucket
        bucket = hash(value) % len(self.hashtable)
        # Store item in list
        bucket_list = self.hashlist[bucket]

        # Update key / value pair if key already in bucket_list
        for key_value in bucket_list:
            if key_value[0] == key:
                key_value[1] = value 
                return True
        # Append value to bucket_list if key not in bucket_list
        key_value = [key, value]
        bucket_list.append(key_value)
        return True
                


        