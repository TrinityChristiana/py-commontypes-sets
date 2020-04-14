# **************************** Challenge: Matching Makes & Models ****************************

print("************ Matching Makes & Models ************************* \n")
"""
Author: Trinity Terry
pyrun: python sets-car.py 
"""

# (make_num, make_name)
makes = (
    (1, "Toyota"), (2, "Nissan"),
    (3, "Ford"), (4, "Mini"),
    (5, "Honda"), (6, "Dodge"),
)

# (model_num, model_name, make_key)
models = (
    (1, "Altima", 2), (2, "Thunderbird", 3),
    (3, "Dart", 6), (4, "Accord", 5),
    (5, "Prius", 1), (6, "Countryman", 4),
    (7, "Camry", 1), (8, "F150", 3),
    (9, "Civic", 5), (10, "Ram", 6),
    (11, "Cooper", 4), (12, "Pilot", 5),
    (13, "Xterra", 2), (14, "Sentra", 2),
    (15, "Charger", 6)
)

# (color_num, color_name)
colors = (
    (1, "Black"), (2, "Charcoal"), (3, "Red"), (4, "Brick"),
    (5, "Blue"), (6, "Navy"), (7, "White"), (8, "Ivory")
)

# (model_key, color_key)
available_car_colors = (
    (1, 1), (1, 2), (1, 7),
    (2, 1), (2, 3), (2, 7),
    (3, 2), (3, 3), (3, 7),
    (4, 3), (4, 5), (4, 8),
    (5, 2), (5, 4), (5, 8),
    (6, 2), (6, 6), (6, 7),
    (7, 1), (7, 3), (7, 7),
    (8, 1), (8, 5), (8, 8),
    (9, 1), (9, 6), (9, 7),
    (10, 2), (10, 5), (10, 7),
    (11, 3), (11, 6), (11, 8),
    (12, 1), (12, 4), (12, 7),
    (13, 2), (13, 6), (13, 8),
    (14, 2), (14, 5), (14, 8),
    (15, 1), (15, 4), (15, 7)
)

# You must first build a new dictionary that follows the format below.
'''
Each key in the dictionary should be the name of a make, and its value will be a dictionary.

The keys in the make dictionary will be the models, and the value will be a list of colors in which that the model is available.

{
    'Toyota': {
      'Prius': ['Charcoal', 'Brick', 'Ivory'],
      'Camry': ['Black', 'Red', 'White']
    },
    'Nissan': {
      'Sentra': ['Charcoal', 'Blue', 'Ivory'],
      'Altima': ['Black', 'Charcoal', 'White'],
      'Xterra': ['Charcoal', 'Navy', 'Ivory']
    },
    'Mini': {
      'Countryman': ['Charcoal', 'Navy', 'White'],
      'Cooper': ['Red', 'Navy', 'Ivory']
    },
    'Ford': {
      'F150': ['Black', 'Blue', 'Ivory'],
      'Thunderbird': ['Black', 'Red', 'White']
    },
    'Honda': {
      'Civic': ['Black', 'Navy', 'White'],
      'Pilot': ['Black', 'Brick', 'White'],
      'Accord': ['Red', 'Blue', 'Ivory']
    },
    'Dodge': {
      'Ram': ['Charcoal', 'Blue', 'White'],
      'Charger': ['Black', 'Brick', 'White'],
      'Dart': ['Charcoal', 'Red', 'White']
    }
}
'''
# Dictionary that will hold the final dictionary
car_dict = dict()

# adds make keys to solution
car_dict = {x[1]:{} for x in makes}

# Adds model key as values in corrospoding make keys
for (model_num, model_name, make_key) in models:
    for (make_num, make_name) in makes:
        if make_num == make_key:
            car_dict[make_name][model_name] = []

# # Will hold the colors to model relationships
model_to_color_dict = {}

# # Adds Model Keys to model_to_color_dict
for (model_num, model_name, make_key) in models:
    model_to_color_dict[model_name] = []

# # Adds color list to each model in model_to_color_dict
for (model_key, color_key) in available_car_colors:
    for (model_num, model_name, make_key) in models:
        if model_key == model_num:
            for (color_num, color_name) in colors:
                if color_num == color_key:
                    model_to_color_dict[model_name].append(color_name)    


# # Merges model_toColor_dict with car_dict by model
for (model, make_collection) in car_dict.items():
    for (make, make_colors) in make_collection.items():
        for (make_to_color_make, make_to_color_colors) in model_to_color_dict.items():
            if make_to_color_make == make:
                car_dict[model][make] = make_to_color_colors
print("\n ****************************** \n Reporting Object \n")
print(car_dict, "\n")

# '''
# Output a report on the command line that looks like this.

# Ford
# ------------------
# F150 available in Black, Blue, Ivory
# Thunderbird available in Black, Red, White

# etc...
# '''

car_report = []
for (model, model_makes_collection) in car_dict.items():
    car_report.extend([model, "------------------"])
    for (make, color_list) in model_makes_collection.items():
        car_report.append(f"{make} available in {', '.join(color_list)}")
    car_report.append("")

print("\n ****************************** \n Command Line Report \n")
print("\n".join(car_report))

