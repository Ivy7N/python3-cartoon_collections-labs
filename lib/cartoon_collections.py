def roll_call_dwarves(dwarf_names):
    for index, name in enumerate(dwarf_names, start=1):
        print(f"{index}. {name}")
dwarf_names = ["Doc", "Dopey", "Bashful", "Grumpy"]
roll_call_dwarves(dwarf_names)

def summon_captain_planet(elements):
    return [element.capitalize() + "!" for element in elements]
elements = ["earth", "fire", "wind", "heart"]
result = summon_captain_planet(elements)
print(result)

def long_planeteer_calls(calls, length_threshold):
    return any(len(call) > length_threshold for call in calls)

short_words = ["puff", "go", "two"]
result_short = long_planeteer_calls(short_words, 3)
print(result_short)

assorted_words = ["two", "go", "industrious", "bop"]
result_assorted = long_planeteer_calls(assorted_words, 5)
print(result_assorted)

def find_the_cheese(items, cheeses):
    for item in items:
        if item in cheeses:
            return item
    return None

snacks = ["crackers", "gouda", "thyme"]
result_snacks = find_the_cheese(snacks, ["gouda", "cheddar", "swiss"])
print(result_snacks) 

soup = ["tomato soup", "cheddar", "oyster crackers", "gouda"]
result_soup = find_the_cheese(soup, ["gouda", "cheddar", "swiss"])
print(result_soup) 

ingredients = ["garlic", "rosemary", "bread"]
result_ingredients = find_the_cheese(ingredients, ["gouda", "cheddar", "swiss"])
print(result_ingredients)  
