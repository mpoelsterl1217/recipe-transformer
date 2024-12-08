import fractions
import re
from different_style import to_chinese_style, to_itlian_style
from step import Step

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
        # print(self.ingredient_list)
        for ingredient in self.ingredient_list:
            ingredient.quantity = handle_single_character_fractions_smh(ingredient.quantity)
            if ingredient.quantity:
                q = float(sum( map( fractions.Fraction, ingredient.quantity.split() ) )) * factor
                if q % 1 == 0:
                    q = int(q)
                ingredient.quantity = str(q)
        
        # update step for scale
        for step in self.steps_list:
            current_usage_list = step.details.get("current_uasge")
            if current_usage_list !=[] and current_usage_list != None:
                for current_usage in current_usage_list:
                    quantity = current_usage.get("quantity")
                    unit = current_usage.get("unit")
                    if quantity:  # Ensure quantity is not None or empty
                        # Compute the new quantity
                        new_quantity = float(fractions.Fraction(quantity)) * factor

                        current_usage["quantity"] = new_quantity

                        # Create the regex dynamically to match the exact quantity
                        regex_pattern = rf"\b{quantity}\b(\s*{unit})?"
                    
                        # Replace the matched quantity with the scaled quantity
                        step.text = re.sub(
                            regex_pattern, 
                            f"{new_quantity} {unit}" if unit else f"{new_quantity}", 
                            step.text
                        )

    def to_chinese(self):
        old_new_ingredient_list = []
        for ingredient in self.ingredient_list:
            old_ingredient = ingredient.ingredient_name
            new_ingredient = to_chinese_style(ingredient.ingredient_name)
            ingredient.ingredient_name = new_ingredient
            old_new_ingredient_list.append([old_ingredient,new_ingredient])
        
        
        new_steps_list=[]
        num=0
        for step in self.steps_list:
            text = step.text
            if step.details.get("ingredients") != None and step.details.get("ingredients") !=[]:
                for i in old_new_ingredient_list:
                    oldname = i[0]
                    newname = i[1]
                    if oldname in text:
                        text = text.replace(oldname, newname)
            # print("wait! :",text)
            new_steps_list.append(Step(num, text, self.ingredient_list))
            # print(new_steps_list[-1].text)
            num+=1
        self.steps_list = new_steps_list
    
    def to_itlian(self):
        old_new_ingredient_list = []
        for ingredient in self.ingredient_list:
            old_ingredient = ingredient.ingredient_name
            new_ingredient = to_itlian_style(ingredient.ingredient_name)
            ingredient.ingredient_name = new_ingredient
            old_new_ingredient_list.append([old_ingredient,new_ingredient])
        
        
        new_steps_list=[]
        num=0
        for step in self.steps_list:
            text = step.text
            if step.details.get("ingredients") != None and step.details.get("ingredients") !=[]:
                for i in old_new_ingredient_list:
                    oldname = i[0]
                    newname = i[1]
                    if oldname in text:
                        text = text.replace(oldname, newname)
            # print("wait! :",text)
            new_steps_list.append(Step(num, text, self.ingredient_list))
            # print(new_steps_list[-1].text)
            num+=1
        self.steps_list = new_steps_list

        # print(self.ingredient_list)

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