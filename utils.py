import math
import numpy as np
from IPython.core.display import display
import pandas as pd

a_nutrients = ['energy_tot', 'saturate', 'salt', 'sugar']
c_nutrients = ['f_fruit_veg', 'fibre', 'protein']

NUTRIENTS = ['fibre', 'protein', 'carb', 'fat', 'salt']


def salt_to_sodium(salt):
    return salt / 2.5 * 1000


def convert_kcal_to_joules(energy):
    return energy * 4.184


def convert_to_100g(nutrient_weight, total_weight):
    return nutrient_weight / total_weight * 100


# df['nutri_score'] = df.apply(calculate_nutrional_score, axis=1)

def calculate_nutripoints_A(grocery_data_row):
    weight = grocery_data_row[NUTRIENTS].sum()
    # print('weight:', weight)
    """Calculate the nutritional score"""
    a = b = c = d = 0
    if grocery_data_row['energy_tot']:
        energy_tot_kj = convert_kcal_to_joules(convert_to_100g(grocery_data_row['energy_tot'], weight))
        # print('energy_tot_kj', energy_tot_kj)
        if energy_tot_kj <= 2058:
            a = 0
        elif energy_tot_kj <= 2090.6:
            a = 1
        elif energy_tot_kj <= 2123.2:
            a = 2
        elif energy_tot_kj <= 2155.8:
            a = 3
        elif energy_tot_kj <= 2188.4:
            a = 4
        elif energy_tot_kj <= 2221:
            a = 5
        else:
            a = 6

    if grocery_data_row['sugar']:
        sugar = convert_to_100g(grocery_data_row['sugar'], weight)
        # print('sugar', sugar)
        if sugar <= 24.35:
            b = 0
        elif sugar <= 26.576:
            b = 1
        elif sugar <= 28.682:
            b = 2
        elif sugar <= 30.848:
             b = 3
        elif sugar <= 33.014:
             b = 4
        elif sugar <= 35.18:
             b = 5
        else: 
             b = 6

    if grocery_data_row['saturate']:
        saturate = convert_to_100g(grocery_data_row['saturate'], weight)
        # c = np.clip(math.floor(saturate), 0, 10)
        if saturate <= 7.79:
                c = 0
        elif saturate <= 8.566:
            c= 1
        elif saturate <= 9.342:
             c = 2
        elif saturate <= 10.118:
             c = 3
        elif saturate <= 10.894:
             c = 4
        elif saturate <= 11.67:
             c = 5
        else: 
             c = 6


    if grocery_data_row['salt']:
        sodium = salt_to_sodium(convert_to_100g(grocery_data_row['salt'], weight))
        # print('sodium', sodium)
        if sodium <= 535.73:
             d = 0
        elif sodium <= 591.588:
             d = 1
        elif sodium <= 647.446:
             d = 2
        elif sodium <=703.304:
             d = 3
        elif sodium <= 759.162:
             d = 4
        elif sodium <= 815.02:
             d = 5
        else:
             d = 6

    # print('protein:', grocery_data_row['protein'], convert_to_100g(grocery_data_row['protein'], weight))
    # print('fibre:', grocery_data_row['fibre'], convert_to_100g(grocery_data_row['fibre'], weight))
    # print('fat:', grocery_data_row['fat'], convert_to_100g(grocery_data_row['fat'], weight))
    # print('carbs:', grocery_data_row['carb'], convert_to_100g(grocery_data_row['carb'], weight))
    # print('salt:', grocery_data_row['salt'], convert_to_100g(grocery_data_row['salt'], weight))

    return a + b + c + d
    #return energy_tot_kj , sugar , saturate , sodium


def calculate_nutripoints_C(grocery_data_row):
    a = b = c = 0

    weight = grocery_data_row[NUTRIENTS].sum()

    if grocery_data_row['fibre']:
        fibre = convert_to_100g(grocery_data_row['fibre'], weight)
        if fibre <= 4.02:
             a = 0
        elif fibre <= 4.364:
             a = 0.5
        elif fibre <= 4.658:
             a = 1
        elif fibre <= 4.952:
             a = 1.5
        elif fibre <= 5.246:
             a = 2
        elif fibre <= 5.54:
             a = 2.5
        else:
             a = 3

    if grocery_data_row['protein']:
        protein = convert_to_100g(grocery_data_row['protein'], weight)
        if protein <= 11.715:
            b = 0
        elif protein <= 13.036:
             b = 0.5
        elif protein <= 14.357:
             b = 1
        elif protein <= 15.678:
             b = 1.5
        elif protein <= 16.999:
             b = 2
        elif protein <= 18.32:
             b = 2.5
        else:
             b = 3

    if grocery_data_row['f_fruit_veg']:

        fruit = grocery_data_row['f_fruit_veg'] * 100
        if fruit <= 21.76:
             c = 0
        elif fruit <= 25.24:
             c = 0.5
        elif fruit <= 28.72:
             c = 1
        elif fruit <= 32.2:
             c = 1.5
        elif fruit <= 35.68:
             c = 2
        elif fruit <= 39.16:
             c = 2.5
        else:
             c = 3
    return a + b + c
    #return [fibre , protein , fruit]


def calculate_nutripoints(grocery_data_row):
    return calculate_nutripoints_A(grocery_data_row) - calculate_nutripoints_C(grocery_data_row)
