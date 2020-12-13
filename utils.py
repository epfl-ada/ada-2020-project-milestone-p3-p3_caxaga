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

def calculate_nutripoints_A(grocery_data_row, min_data, max_data):
    weight = grocery_data_row[NUTRIENTS].sum()
    # print('weight:', weight)
    """Calculate the nutritional score"""
    a = b = c = d = 0
    if grocery_data_row['energy_tot']:
        min_energy_tot = convert_kcal_to_joules(
            convert_to_100g(min_data['energy_tot'], weight))
        max_energy_tot = convert_kcal_to_joules(
            convert_to_100g(max_data['energy_tot'], weight))
        interval_energy = (max_energy_tot - min_energy_tot) / 6
        energy_tot_kj = convert_kcal_to_joules(
            convert_to_100g(grocery_data_row['energy_tot'], weight))

        for i in range(1, 7):
            if energy_tot_kj <= min_energy_tot + i * interval_energy:
                a = i - 1
                break

    if grocery_data_row['sugar']:
        sugar = convert_to_100g(grocery_data_row['sugar'], weight)
        min_sugar = convert_to_100g(min_data['sugar'], weight)
        max_sugar = convert_to_100g(max_data['sugar'], weight)
        interval_sugar = (max_sugar - min_sugar) / 6

        for i in range(1, 7):
            if sugar <= min_sugar + i * min_sugar:
                b = i - 1
                break

    if grocery_data_row['saturate']:
        saturate = convert_to_100g(grocery_data_row['saturate'], weight)
        min_saturate = convert_to_100g(min_data['saturate'], weight)
        max_saturate = convert_to_100g(max_data['saturate'], weight)
        interval_saturate = (max_saturate - min_saturate) / 6

        for i in range(1, 7):
            if saturate <= min_saturate + i * interval_saturate:
                c = i - 1
                break

    if grocery_data_row['salt']:
        sodium = salt_to_sodium(convert_to_100g(
            grocery_data_row['salt'], weight))
        min_sodium = salt_to_sodium(
            convert_to_100g(min_data['salt'], weight))
        max_sodium = salt_to_sodium(convert_to_100g(max_data['salt'], weight))
        interval_sodium = (max_sodium - min_sodium) / 6

        for i in range(1, 7):
            if sodium <= min_sodium + i * interval_sodium:
                d = i - 1
                break

    # print('protein:', grocery_data_row['protein'], convert_to_100g(grocery_data_row['protein'], weight))
    # print('fibre:', grocery_data_row['fibre'], convert_to_100g(grocery_data_row['fibre'], weight))
    # print('fat:', grocery_data_row['fat'], convert_to_100g(grocery_data_row['fat'], weight))
    # print('carbs:', grocery_data_row['carb'], convert_to_100g(grocery_data_row['carb'], weight))
    # print('salt:', grocery_data_row['salt'], convert_to_100g(grocery_data_row['salt'], weight))

    return a + b + c + d
    # return energy_tot_kj , sugar , saturate , sodium


def calculate_nutripoints_C(grocery_data_row, min_data, max_data):
    a = b = c = 0

    weight = grocery_data_row[NUTRIENTS].sum()

    if grocery_data_row['fibre']:
        fibre = convert_to_100g(grocery_data_row['fibre'], weight)
        min_fibre = convert_to_100g(min_data['fibre'], weight)
        max_fibre = convert_to_100g(max_data['fibre'], weight)
        interval_fibre = (max_fibre - min_fibre) / 6
                                    
        for i in range(1, 7):
            if fibre <= min_fibre + i * interval_fibre:
                a = (i - 1) * 0.5
                break

    if grocery_data_row['protein']:
        protein = convert_to_100g(grocery_data_row['protein'], weight)
        min_protein = convert_to_100g(min_data['protein'], weight)
        max_protein = convert_to_100g(max_data['protein'], weight)
        interval_protein = (max_protein - min_protein) / 6

        for i in range(1, 7):
            if protein <= min_protein + i * interval_protein:
                b = (i - 1) * 0.5
                break

    if grocery_data_row['f_fruit_veg']:
        fruit = grocery_data_row['f_fruit_veg'] * 100
        min_fruit = convert_to_100g(min_data['f_fruit_veg'], weight)
        max_fruit = convert_to_100g(max_data['f_fruit_veg'], weight)
        interval_fruit = (max_fruit - min_fruit) / 6

        for i in range(1, 7):
            if fruit <= min_fruit + i * interval_fruit:
                c = (i - 1) * 0.5
                break

    return a + b + c
    # return [fibre , protein , fruit]


def calculate_nutripoints(grocery_data_row, min_data, max_data):
    return calculate_nutripoints_A(grocery_data_row, min_data, max_data) - calculate_nutripoints_C(grocery_data_row, min_data, max_data)
