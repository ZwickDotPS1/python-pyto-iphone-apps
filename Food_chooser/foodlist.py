
import random
import time

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
    x = (len(food))-1
    f = random.randint(0, x)
    foodchoice = food[f]
    lunchfoodchoice = lunchfood[f]
    
    if val == 'd' :
        print(foodchoice)
        time.sleep(5)
        menu()
        
    elif val == 'l' :
        print(lunchfoodchoice)
        time.sleep(5)
        menu()
    else :
        print('invalid input, press l or d to continue.')
        time.sleep(5)
        menu()
        
menu()
