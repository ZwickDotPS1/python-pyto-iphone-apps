#import random

import requests

def diceroll(x):    
    dieroll = (f"https://www.random.org/integers/?num=1&min=1&max={x}&col=5&base=10&format=plain&rnd=new")
    number = requests.get(dieroll)
    number = int(number.text)
    rollstr = print(f"You rolled a {number}")

def menu() :
    print(' 1: d20  2: d12  3: d10 \n 4: d8   5: d6   6: d4 \n 7: d100 q: quit')
    print('\n')
    dice = input('What kind of dice do you want to roll?\n')
    if dice == "1":
        print(diceroll(20))
        menu()
    elif dice == "2":
        print(diceroll(12))
        menu()
    if dice == "3":
        print(diceroll(10))
        menu()
    if dice == "4":
        print(diceroll(8))
        menu()
    if dice == "5":
        print(diceroll(6))
        menu()
    if dice == "6":
        print(diceroll(4))
        menu()
    if dice == "7":
        print(diceroll(100))
        menu()
    if dice == "q":
        return
    else :
        print('Invalid choice')
        print('')
        menu()

menu()