import random

meats = ["chicken breast", "chicken thighs", "duck", "roast duck", "beef brisket", "ground beef", "pork belly", 
    "pork loin", "lamb chops", "goat meat", "turkey", "shrimp", "crab", "lobster", "scallops", "clams", 
    "oysters", "mussels", "salmon", "tuna", "mackerel", "sardines", "eel", "tilapia", "trout", "catfish", 
    "chicken", "steak", "pork", "lamb", "mutton", "sausage", "meatballs", "meatball", "meat", "veal",
    "vennison", "beef", "ham", "deli ham", "bacon", "steamed bacon"]

vegetarian_substitutes = ["tofu", "seitan", "tempeh", "jackfruit"]

def is_meat(ingredient):
    if ingredient in meats:
        return True
    for m in ["chicken", "ham", "steak", "veal", "beef", "pork", "salmon", "tuna", "meat", "bacon"]:
        if m in ingredient.split():
            return True
    return False

def meat_replace(ingredient):
    if "steak" or "ground beef" or "ground veal" or "ground pork" in ingredient.split():
        return "seitan"
    else:
        return "tofu"

def is_vegetarian(ingredient):
    for s in vegetarian_substitutes:
        if s in ingredient:
            return True
    return False

def veg_replace(ingredient):
    if "seitan" in ingredient.split():
        return "steak"
    else:
        return random.choice(["chicken", "lamb", "turkey"])
