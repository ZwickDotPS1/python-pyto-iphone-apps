import random
import csv

with open('streets.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    streets = []
    for row in csv_reader:
        streets.append(row)

with open('austinzip.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    zipcode = []
    for row in csv_reader:
        zipcode.append(row)

# address_funct:
print("generating addresses")
b = (len(streets))+1 
c = random.randint(0, b)
f = random.randint(2, 4)    
if (f == 2) :
    streetnum = random.randint(10, 99)
elif (f == 3) :
    streetnum = random.randint(100, 999)
else :
    streetnum = random.randint(1000, 9999)
streetz = streets[c]
address = (f'{streetnum} + {streetz}')

 # zipcode
k = (len(zipcode))
h = random.randint(0, k)
j = h + 1
zip = zipcode[h]
city = zipcode[j]
print(address)
print(city)