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

# name_funct(name) :
print("generating names")
x = (len(firstname))
y = (len(lastname))
f = random.randint(0, x)
g = random.randint(0, y)
fname = firstname[f]
lname = lastname[g]
name = (f'{fname} {lname}')


