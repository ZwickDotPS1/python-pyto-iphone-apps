
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

food = [
    "Turkey tacos", 
    "Pasta and sauce", 
    "Asian stir-fry", 
    "Grilled sausage", 
    "Sandwiches", 
    "Baked chicken and veggies", 
    "Burgers", 
    "Chili", 
    "Hot pot", 
    "Breakfast for dinner", 
    "Garden salad with chicken",
    "Pizza",
    "Salmon and veggies",
    "Roasted veggies and chicken"
    ]
    
lunchfood = [
    "Turkey tacos", 
    "Pasta and sauce", 
    "Grilled sausage", 
    "Sandwich", 
    "Veggie Burgers", 
    "Chili", 
    "Garden salad with chicken",
    "Pizza",
    "Ramen",
    "Leftovers"
    ]

def menu() :
    print("Hi! I'm the food helper!")
    main_funct()

def main_funct() :
    val = input("Is it time for [L]unch or [D]inner?")
    x = (len(food))
    f = random.randint(0, x)
    foodchoice = food[f]
    lunchfoodchoice = lunchfood[f]
    
    if val == 'd' :
        print(foodchoice)
        time.sleep(5)
        return foodchoice
        
    elif val == 'l' :
        print(lunchfoodchoice)
        time.sleep(5)
        return foodchoice
    else :
        print('invalid input, press l or d to continue.')
        time.sleep(5)
        menu()

#start again in case user is unhappy
def restart():
    sa = input('Run again? Y/N')
    if sa == 'y':
        menu()
    elif sa == 'n':
        return
    else:
        return

fc_log(menu())
restart()
