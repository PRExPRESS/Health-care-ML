from flask import Flask, request, jsonify
import numpy as np
import joblib
from finalDiseases import filter_diesease
from finalFoodItems import recommend_food_items


app = Flask(__name__)

# calculating the bmr
def calculate_bmr(weight, height, age, gender):
    if gender == 'Male':
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    if gender == 'Female':
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
    return bmr

# calculating caloriy intake per day
def calculate_calories(bmr):
    calorie = 1.2 * bmr
    return calorie

# calculate nutrition level based on diease
def calculate_dieseas_nutrion_level(diease):
    carbs = 250
    fat = 100
    protein = 100
    if diease == 'none':
        carbs = 250
        fat = 100
        protein = 101
    else:
        diesease_data = filter_diesease(diease)
        dieses_carb = diesease_data['Carbs'].values[0]
        dieses_fat = diesease_data['Total Fat'].values[0]
        dieses_protein = diesease_data['Protein'].values[0]

        if dieses_carb < carbs:
            carbs = dieses_carb
        if dieses_fat < carbs:
            fat = dieses_fat
        if dieses_protein < protein:
            protein = dieses_protein
    # print (carbs,fat,protein)
    return {carbs,fat,protein}


def mealtime_calculation(mealtime,nutrionlevel):
    if mealtime == 'Breakfast':
      data =  max_breakfast(nutrionlevel)
    if mealtime == 'Lunch':
       data = max_lunch(nutrionlevel)
    if mealtime == 'Snacks':
        data = max_snack(nutrionlevel)
    if mealtime == 'Dinner':
        data = max_dinner(nutrionlevel)
    return data

def calculate_nutrition(calorie, nutrionLevel):
    multiplier = calorie/ 2200
    carbs = list(nutrionLevel)[0] * multiplier
    fat = list(nutrionLevel)[1] * multiplier
    protein = list(nutrionLevel)[2] * multiplier
    return {carbs, fat, protein}

def max_breakfast(nutrions):
    # nutrions = calculate_nutrition(bmr,nutrionLevel)
    
    carbs = list(nutrions)[0] * 0.37
    fat = list(nutrions)[1]* 0.3
    protein = list(nutrions)[2]* 0.37
    calories = (fat * 8) + (carbs * 4) + (protein * 4)
    return {carbs, fat, protein, calories}
    
def max_lunch(nutrions):
    # nutrions = calculate_nutrition(bmr,nutrionLevel)
    carbs = list(nutrions)[0] * 0.35
    fat = list(nutrions)[1]* 0.35
    protein = list(nutrions)[2]* 0.3
    calories = (fat * 8) + (carbs * 4) + ( protein * 4)
    return {carbs, fat, protein, calories}

def max_snack(nutrions):
    # nutrions = calculate_nutrition(bmr,nutrionLevel)
    carbs = list(nutrions)[0] * 0.1
    fat = list(nutrions)[1]* 0.1
    protein = list(nutrions)[2]* 0.05
    calories = (fat * 8) + (carbs * 4) + ( protein * 4)
    return {carbs, fat, protein, calories}

def max_dinner(nutrions):
    # nutrions = calculate_nutrition(bmr,nutrionLevel)
    carbs = list(nutrions)[0] * 0.35
    fat = list(nutrions)[1]* 0.25
    protein = list(nutrions)[2]* 0.28
    calories = (fat * 8) + (carbs * 4) + ( protein * 4)
    return {carbs, fat, protein, calories}

def req_food(foodtype):
    if foodtype == "Non-veg":
        data = ['Fruits', 'Grains', 'Vegetables', 'Meat', 'Protein', 'Beverages']
    if foodtype == 'Veg':
        data = ['Fruits', 'Grains', 'Vegetables', 'Protein', 'Beverages']
    return data

def recommended_items(user_requirement):
    data = recommend_food_items(user_requirement)
    return data
    
    

