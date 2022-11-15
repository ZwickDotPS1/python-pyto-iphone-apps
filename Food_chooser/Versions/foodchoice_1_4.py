
import random
import time

import os.path
import datetime

# creates dt object to make a datestamp
rawdate = datetime.datetime.now()
dt = rawdate.strftime("%x %I:%M %p %Z")

# block checks to see if log file exists and if not creates one before writing

def new_logfile() :
    f = open("fc_log.txt", "w")
    f.close()

def write_logfile(x):
    f = open("fc_log.txt", "a")
    f.write(f'{dt}{x}\n')
    f.close()
    
def fc_log(x): #add function name 
    if os.path.isfile('fc_log.txt') == True :
        write_logfile(x)
    else :
        new_logfile()
        write_logfile(x)

#pulls values from dinner.txt
g = open("dinner.txt", "r")
data = g.readlines()
food = []
for row in data:
    size = len(row)
    # Slice string to remove \n from string before putting into list
    row = row[:size - 1]
    food.append(row)
g.close()
    
#gets values from lunch.txt
h = open("lunch.txt", "r")
data = h.readlines()
lunchfood = []
for row in data:
    size = len(row)
    row = row[:size - 1]
    lunchfood.append(row)
h.close()

#menu function
def menu() :
    print("Hi! I'm the food helper!")
    main_funct()

def main_funct() :
    val = input("Is it time for [L]unch or [D]inner?")
    x = (len(food))
    f = random.randint(0, x)
    foodchoice = food[f-1]
    lunchfoodchoice = lunchfood[f-1]
    
    if val == 'd' :
        print(foodchoice)
        time.sleep(2)
        return foodchoice
        
    elif val == 'l' :
        print(lunchfoodchoice)
        time.sleep(2)
        return lunchfoodchoice
    else :
        print('invalid input, press l or d to continue.')
        time.sleep(2)
        menu()

#start again in case user is unhappy
def restart():
    sa = input('Run again? Y/N\n')
    if sa == 'y':
        menu()
    elif sa == 'n':
        return
    else:
        return

fc_log(main_funct())
fc_log(restart())
