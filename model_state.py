import fractions

class State:
    def __init__(self, steps_list, ingredient_list):
        self.steps_list = steps_list
        self.ingredient_list = ingredient_list
        self.in_steps = False
        self.current_step = None
        self.input_history = []
        self.output_history = []

    def scale_recipe(self, factor):
        # ["[0-9]", "[½⅓⅔¼¾⅛⅜⅝⅞]"]
        print(self.ingredient_list)
        for ingredient in self.ingredient_list:
            ingredient.quantity = handle_single_character_fractions_smh(ingredient.quantity)
            if ingredient.quantity:
                q = float(sum( map( fractions.Fraction, ingredient.quantity.split() ) )) * factor
                if q % 1 == 0:
                    q = int(q)
                ingredient.quantity = str(q)
        print(self.ingredient_list)

def handle_single_character_fractions_smh(q):
    result = q
    for c in q:
        if c in "½⅓⅔¼¾⅛⅜⅝⅞":
            result = result.replace(c, convert_single_character_fractions_smh(c))
    return result

def convert_single_character_fractions_smh(frac):
    if frac == "½":
        return "1/2"
    elif frac == "⅓":
        return "1/3"
    elif frac == "⅔":
        return "2/3"
    elif frac == "¼":
        return "1/4"
    elif frac == "¾":
        return "3/4"
    elif frac == "⅛":
        return "1/8"
    elif frac == "⅜":
        return "3/8"
    elif frac == "⅝":
        return "5/8"
    elif frac == "⅞":
        return "7/8"