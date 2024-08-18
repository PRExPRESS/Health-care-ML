import os
import pandas as pd

data = pd.read_csv('dataset\Calorie_value.csv')
food = pd.read_csv('dataset\input.csv')

combined_data = pd.merge(data, food, on='food items')

def filter_by_category(category):
    filtered_data = data[data["Category"] == category]
    return filtered_data



