import random

ingredient_categories = {
    "proteins" : [
    "tofu", "tempeh", "seitan", "soybeans", "edamame", "textured vegetable protein (TVP)", "soy curls",
    "chicken breast", "chicken thighs", "duck", "roast duck", "beef brisket", "ground beef", "pork belly", 
    "pork loin", "lamb chops", "goat meat", "turkey", "shrimp", "crab", "lobster", "scallops", "clams", 
    "oysters", "mussels", "salmon", "tuna", "mackerel", "sardines", "eel", "tilapia", "trout", "catfish", 
    "century eggs", "salted duck eggs", "quail eggs", "chickpeas", "lentils", "black beans", "kidney beans", 
    "adzuki beans", "mung beans", "pinto beans", "navy beans", "fava beans"],

    "vegetables" : [
    "bok choy", "napa cabbage", "broccoli", "mustard greens", "spinach", "kale", "lettuce", 
    "romaine lettuce", "arugula", "Swiss chard", "carrots", "beets", "radishes", "daikon radish", "lotus root", 
    "ginger root", "garlic", "onions", "red onions", "green onions", "shallots", "leeks", 
    "potatoes", "sweet potatoes", "yams", "taro", "cassava", "burdock root", "zucchini", "cucumbers", 
    "bell peppers", "eggplant", "broccoli", "cauliflower", 
    "mushrooms", "snow peas", "sugar snap peas", 
    "green beans", "asparagus", "bamboo shoots", "water chestnuts", "celery", "tomatoes", "okra", "fennel"],

    "herbs_and_spices" : [
    "cilantro", "parsley", "basil", "Thai basil", "mint", "dill", "thyme", "oregano", "rosemary", "tarragon", 
    "scallions", "chives", "bay leaves", "star anise", "cinnamon sticks", "cloves", 
    "cardamom", "fennel seeds", "cumin seeds", "fenugreek", "turmeric", "ginger", "garlic", "chili flakes", 
    "dried chilies", "Sichuan peppercorns", "white pepper", "black pepper", "paprika", "smoked paprika", 
    "cayenne pepper", "nutmeg", "mace", "allspice", "mustard seeds", "coriander seeds", "caraway seeds", 
    "sumac", "lemongrass", "galangal", "vanilla beans", "saffron", "wasabi powder", "horseradish"],

    "fruits" : [
    "apples", "pears", "bananas", "oranges", "mandarins", "tangerines", "grapefruits", "lemons", "limes", 
    "mangoes", "pineapples", "papayas", "dragon fruit", "lychees", "longan", "jackfruit", "durian", "passion fruit", 
    "grapes", "kiwis", "strawberries", "blueberries", "blackberries", "raspberries", 
    "cranberries", "pomegranates", "peaches", "plums", "cherries", "apricots", "nectarines", "persimmons", 
    "figs", "dates", "coconuts", "melons", "avocados", "guava", "starfruit"],

    "grains_and_starches" : [
    "rice", "quinoa", 
    "barley", "wheat berries", "bulgur wheat", "millet", "amaranth", "farro", "buckwheat", "cornmeal", 
    "polenta", "grits", "oats", "flour", "vermicelli noodles", "egg noodles", "wheat noodles (lo mein)", 
    "rice noodles", "glass noodles", "udon noodles", "soba noodles", "instant ramen", 
    "sweet potatoes", "cassava", "tapioca", "potato starch", "arrowroot starch", "cornstarch"],

    "condiments" : [
    "soy sauce ", "oyster sauce", "hoisin sauce", "fish sauce", 
    "black vinegar", "rice vinegar", "white vinegar", "plum sauce", "sweet bean paste", 
    "doubanjiang", "fermented black beans", "XO sauce", "chili oil", 
    "Lao Gan Ma", "miso paste", "ketchup", "mustard", 
    "mayonnaise", "sriracha", "barbecue sauce", "teriyaki sauce", "tartar sauce", "worcestershire sauce", 
    "honey mustard", "tahini", "peanut butter", "almond butter", "black sesame paste", "tomato-basil pasta sauce", "pasta sauce"]

}

chinese_style = {
    "proteins" : [
    "tofu", "silken tofu", "fermented tofu", "tempeh", "seitan", "soybeans", 
    "century eggs", "salted duck eggs", "Peking duck", "roast pork", "ground pork", 
    "beef shank", "pork belly", "duck", "chicken thighs", "shrimp", "dried shrimp", 
    "scallops", "crab", "eel", "fish balls", "Chinese sausage", "dried fish"],

    "vegetables" : [
    "bok choy", "napa cabbage", "Chinese broccoli", "choy sum", "mustard greens", 
    "lotus root", "daikon radish", "water spinach", "bamboo shoots", "water chestnuts", 
    "winter melon", "shiitake mushrooms", "wood ear mushrooms", "enoki mushrooms", 
    "snow peas", "Chinese eggplant", "taro", "garlic chives", "Chinese celery", 
    "yam", "bitter melon"],

    "fruits" : [
    "lychee", "longan", "dragon fruit", "jackfruit", "durian", "pomelo", 
    "mandarin orange", "Chinese pear", "persimmon", "jujube", "starfruit", 
    "hawthorn", "mango", "pineapple", "watermelon", "honeydew melon", "coconut", 
    "apple", "plum"],

    "herbs_and_spices" : [
    "ginger", "garlic", "scallions", "cilantro", "Chinese chives", "star anise", 
    "Sichuan peppercorns", "cinnamon", "cloves", "bay leaves", "white pepper", 
    "dried chilies", "cumin seeds", "fennel seeds", "mustard seeds", "lemongrass"],

    "grains_and_starches" : [
    "white rice", "jasmine rice", "sticky rice", "black rice", "millet", 
    "rice noodles", "glass noodles", "wheat noodles", "hand-pulled noodles", 
    "egg noodles", "udon noodles", "sweet potato starch", "tapioca starch", 
    "potato starch"],

    "condiments" : [
    "light soy sauce", "dark soy sauce", "oyster sauce", "hoisin sauce", 
    "black vinegar", "rice vinegar", "plum sauce", "fermented black beans", 
    "chili oil", "Doubanjiang", "sweet bean paste", "Shaoxing wine", "XO sauce", 
    "sesame oil", "fermented tofu"]

}

italian_style = {
    "proteins": [
        "chicken breast", "pork loin", "ground beef", "veal", "Italian sausage", 
        "prosciutto", "pancetta", "salami", "bresaola", "mortadella", 
        "anchovies", "tuna", "clams", "mussels", "calamari", "shrimp", 
        "scallops", "eggplant (as a protein substitute)", "ricotta cheese", 
        "mozzarella cheese", "parmesan cheese", "pecorino romano"
    ],

    "vegetables": [
        "tomatoes", "zucchini", "bell peppers", "artichokes", "eggplant", 
        "spinach", "kale", "arugula", "fennel", "mushrooms", 
        "onions", "garlic", "leeks", "carrots", "celery", "radicchio", 
        "cherry tomatoes", "olives", "capers", "basil leaves"
    ],

    "fruits": [
        "lemons", "oranges", "figs", "grapes", "apples", "pears", 
        "peaches", "plums", "strawberries", "blueberries", "blackberries", 
        "melons", "pomegranates", "apricots", "cherries", "citrus zest"
    ],

    "herbs_and_spices": [
        "basil", "oregano", "rosemary", "thyme", "parsley", "sage", 
        "marjoram", "bay leaves", "fennel seeds", "chili flakes", 
        "black pepper", "white pepper", "nutmeg", "garlic", "onion powder"
    ],

    "grains_and_starches": [
        "spaghetti", "penne", "fettuccine", "lasagna sheets", "risotto rice (Arborio)", 
        "orzo", "farro", "polenta", "gnocchi", "pappardelle", 
        "tagliatelle", "linguine", "tortellini", "ravioli", "semolina flour", 
        "all-purpose flour", "breadsticks", "ciabatta", "focaccia", "couscous"
    ],

    "condiments": [
        "olive oil", "extra virgin olive oil", "balsamic vinegar", "red wine vinegar", 
        "tomato paste", "marinara sauce", "pesto", "alfredo sauce", "capers", 
        "anchovy paste", "sun-dried tomatoes", "truffle oil", "garlic oil", 
        "Parmesan cheese (grated)", "ricotta", "mascarpone"
    ]
}


def find_category(ingredient_name):
    for category, sublist in ingredient_categories.items():
        for i in sublist:
            if (ingredient_name.lower() in i) or (i in ingredient_name.lower()):
                return category
    return None

def to_chinese_style(ingredient_name):
    category = find_category(ingredient_name)
    if category != None:
        ingredient_list = chinese_style.get(category)
        random_element = random.choice(ingredient_list)
    else:
        ingredient_list = chinese_style.get("condiments")
        random_element = random.choice(ingredient_list)
    
    return random_element

def to_itlian_style(ingredient_name):
    category = find_category(ingredient_name)
    if category != None:
        ingredient_list = italian_style.get(category)
        random_element = random.choice(ingredient_list)
    else:
        ingredient_list = italian_style.get("condiments")
        random_element = random.choice(ingredient_list)
    
    return random_element

# print(to_chinese("pasta sauce"))

# print(to_itlian("rice"))