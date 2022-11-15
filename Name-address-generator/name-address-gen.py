import random
import csv

with open('firstnames.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    firstname = []
    for row in csv_reader:
        firstname.append(row)
    
with open('surnames.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    lastname = []
    for row in csv_reader:
        lastname.append(row)

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

cnt = 0
for cnt in range(0,99) :
    # name_funct(name) :
    x = (len(firstname))-1
    y = (len(lastname))-1
    f = random.randint(0, x)
    g = random.randint(0, y)
    fname = firstname[f]
    lname = lastname[g]
    name = (f'{fname} {lname}')

    # address_funct:
    b = (len(streets))-1
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
    k = (len(zipcode))-1
    h = random.randint(0, k-1)
    j = h + 1
    zip = zipcode[h]
    if j > 74 : j = 74
    city = zipcode[j]
    print(name)
    print(address)
    print(city)
    print("")
    cnt = cnt + 1
