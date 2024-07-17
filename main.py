import csv 

# Read Address CSV file
# Attribution: https://docs.python.org/3/library/csv.html
with open("csv-files/addressCSV.csv") as addressCSV:
    ReadAddress = list(csv.reader(addressCSV))

with open("csv-files/distanceCSV.csv") as distanceCSV:
    ReadDistance = list(csv.reader(distanceCSV))

with open("csv-files/packageCSV.csv") as packageCSV: 
    ReadPackage = list(csv.reader(packageCSV))