import pyto_ui as ui
import random

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
        "Salmon and veggies"
        ]

x = (len(food))-1
f = random.randint(0, x)
foodchoice = food[f]

class View(ui.VerticalStackView):

    def label(self) -> ui.Label:
        label = ui.Label()
        label.text = foodchoice
        label.font = ui.Font.bold_system_font_of_size(20)
        return label

    def __init__(self):
        super().__init__()

        self.add_subview(self.label())
 

view = View()
ui.show_view(view, ui.PRESENTATION_MODE_FULLSCREEN)
