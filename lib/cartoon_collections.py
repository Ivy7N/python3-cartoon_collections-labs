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
calls = ["earth", "fire", "wind", "water"]
result = long_planeteer_calls(calls, 5)
print(result)

def find_the_cheese(items, cheeses):
    for item in items:
        if item in cheeses:
            return item
    return None  

items = ["crackers", "cheddar", "apple", "swiss"]
cheeses = ["cheddar", "swiss", "gouda"]
result = find_the_cheese(items, cheeses)
print(result)
