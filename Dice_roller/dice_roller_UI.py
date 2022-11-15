
import qrandom

import pyto_ui as ui



roll=0

def menu() :
    print('1: d20, 2: d12, 3: d10, 4: d8, 5: d6 6: d4')
    dice = input('What kind of dice do you want to roll?\n')
    if dice == "1":
        print(qrandom.sample(range(20)))
        menu()
    elif dice == "2":
        print(qrandom.sample(range(12)))
        menu()
    if dice == "3":
        print(qrandom.sample(range(20))))
        menu()
    if dice == "4":
        print(qrandom.sample(range(8)))
        menu()
    if dice == "5":
        print(qrandom.sample(range(6)))
        menu()
    if dice == "6":
        print(qrandom.sample(range(4)))
        menu()
    else :
        print('Invalid option')
        menu()


#class View(ui.VerticalStackView):

#    def label(self) -> ui.Label:
#        label = ui.Label()
#        label.text = "Dice Roller"
#        label.font = ui.Font.bold_system_font_of_size(20)
#        return label
    
#    def desc(self) -> ui.Label:
#        desc = ui.Label()
#        desc.text = f"{roll} appears here"
#        desc.font = ui.Font.bold_system_font_of_size(16)
#        return desc
    
#    def d20(self) -> ui.Button():
#        d20 = ui.Button()
#        d20.title="d20"
#        d20.size = (100, 50)
#        d20.flex = [
#            ui.FLEXIBLE_BOTTOM_MARGIN,
#            ui.FLEXIBLE_TOP_MARGIN,
#            ui.FLEXIBLE_LEFT_MARGIN,
#            ui.FLEXIBLE_RIGHT_MARGIN
#        ]
#        d20.action = d20roll()
#        return d20

#    def __init__(self):
#        super().__init__()

#        self.add_subview(self.label())
#        self.add_subview(self.desc())
#        self.add_subview(self.d20())

def menu() :
    print('1: d20, 2: d12, 3: d10, 4: d8, 5: d6 6: d4')
    dice = input('What kind of dice do you want to roll?\n')
    if dice == "1":
        print(random.randint(1, 20))
        menu()
    elif dice == "2":
        print(random.randint(1, 12))
        menu()
    if dice == "3":
        print(random.randint(1, 10))
        menu()
    if dice == "4":
        print(random.randint(1, 8))
        menu()
    if dice == "5":
        print(random.randint(1, 6))
        menu()
    if dice == "6":
        print(random.randint(1, 4))
        menu()
    else :
        print('Invalid option')
        menu()
        
def d20roll() :
    roll=random.randint(1,20)
    return

view = View()
ui.show_view(view, ui.PRESENTATION_MODE_FULLSCREEN)
menu()