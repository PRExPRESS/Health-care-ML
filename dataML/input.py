import pandas as pd

data = pd.read_csv('dataset\input.csv')

def filter_meal_time(meal_time):
    filtered_data = data[data[meal_time] == 1]
    return filtered_data

def filter_food(food):
    filtered_data = data[data["Food_items"] == food]
    return filtered_data
