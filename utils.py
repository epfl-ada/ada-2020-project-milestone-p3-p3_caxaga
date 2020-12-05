import math
import numpy as np
from IPython.core.display import display

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
        # if energy_tot_kj <= 335:
        #     a = 0
        # elif energy_tot_kj <= 670:
        #     a = 1
        # elif energy_tot_kj <= 1005:
        #     a = 2
        # elif energy_tot_kj <= 1340:
        #     a = 3
        # elif energy_tot_kj <= 1675:
        #     a = 4
        # elif energy_tot_kj <= 2010:
        #     a = 5
        # elif energy_tot_kj <= 2345:
        #     a = 6
        # elif energy_tot_kj <= 2680:
        #     a = 7
        # elif energy_tot_kj <= 3015:
        #     a = 8
        # elif energy_tot_kj <= 3350:
        #     a = 9
        # else:
        #     a = 10

    if grocery_data_row['sugar']:
        sugar = convert_to_100g(grocery_data_row['sugar'], weight)
        # print('sugar', sugar)
        # if sugar <= 4.5:
        #     b = 0
        # elif sugar <= 9:
        #     b = 1
        # elif sugar <= 13.5:
        #     b = 2
        # elif sugar <= 18:
        #     b = 3
        # elif sugar <= 22.5:
        #     b = 4
        # elif sugar <= 27:
        #     b = 5
        # elif sugar <= 31:
        #     b = 6
        # elif sugar <= 36:
        #     b = 7
        # elif sugar <= 40:
        #     b = 8
        # elif sugar <= 45:
        #     b = 9
        # else:
        #     b = 10

    if grocery_data_row['saturate']:
        saturate = convert_to_100g(grocery_data_row['saturate'], weight)
        # c = np.clip(math.floor(saturate), 0, 10)

    if grocery_data_row['salt']:
        sodium = salt_to_sodium(convert_to_100g(grocery_data_row['salt'], weight))
        # print('sodium', sodium)
        # if sodium <= 90:
        #     d = 0
        # elif sodium <= 180:
        #     d = 1
        # elif sodium <= 270:
        #     d = 2
        # elif sodium <= 360:
        #     d = 3
        # elif sodium <= 450:
        #     d = 4
        # elif sodium <= 540:
        #     d = 5
        # elif sodium <= 630:
        #     d = 6
        # elif sodium <= 720:
        #     d = 7
        # elif sodium <= 810:
        #     d = 8
        # elif sodium <= 800:
        #     d = 9
        # else:
        #     d = 10

    # print('protein:', grocery_data_row['protein'], convert_to_100g(grocery_data_row['protein'], weight))
    # print('fibre:', grocery_data_row['fibre'], convert_to_100g(grocery_data_row['fibre'], weight))
    # print('fat:', grocery_data_row['fat'], convert_to_100g(grocery_data_row['fat'], weight))
    # print('carbs:', grocery_data_row['carb'], convert_to_100g(grocery_data_row['carb'], weight))
    # print('salt:', grocery_data_row['salt'], convert_to_100g(grocery_data_row['salt'], weight))

    # return a + b + c + d
    return energy_tot_kj + sugar + saturate + sodium


def calculate_nutripoints_C(grocery_data_row):
    a = b = c = 0

    weight = grocery_data_row[NUTRIENTS].sum()

    if grocery_data_row['fibre']:
        fibre = convert_to_100g(grocery_data_row['fibre'], weight)
        # if fibre <= 0.7:
        #     a = 0
        # elif fibre <= 1.4:
        #     a = 1
        # elif fibre <= 2.1:
        #     a = 2
        # elif fibre <= 2.8:
        #     a = 3
        # elif fibre <= 3.5:
        #     a = 4
        # else:
        #     a = 5

    if grocery_data_row['protein']:
        protein = convert_to_100g(grocery_data_row['protein'], weight)
        # if protein <= 1.6:
        #     b = 0
        # elif protein <= 3.2:
        #     b = 1
        # elif protein <= 4.8:
        #     b = 2
        # elif protein <= 6.4:
        #     b = 3
        # elif protein <= 8:
        #     b = 4
        # else:
        #     b = 5

    if grocery_data_row['f_fruit_veg']:

        fruit = grocery_data_row['f_fruit_veg'] * 100
        # if fruit <= 40:
        #     c = 0
        # elif fruit <= 60:
        #     c = 1
        # elif fruit <= 80:
        #     c = 2
        # else:
        #     c = 5
    # return a + b + c
    return fibre + protein + fruit


def calculate_nutripoints(grocery_data_row):
    return calculate_nutripoints_A(grocery_data_row) - calculate_nutripoints_C(grocery_data_row)
