# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# import joblib

# # Load your data
# final_foods = pd.read_csv("dataset/complete_food_items.csv")
# calorie_value = pd.read_csv('dataset/Calorie_value.csv')

# # Merge the data
# combined_data = pd.merge(calorie_value, final_foods, on='food items')

# # Define features and target
# features = combined_data.drop(['Category', 'food items'], axis=1)  # Drop non-numeric columns
# target = combined_data['Category']

# # Split the data
# X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=0)

# # Initialize classifier
# classifier = RandomForestClassifier()

# # Fit the model
# classifier.fit(X_train, y_train)

# # Define a function to calculate remaining nutritional requirements
# def calculate_requirements(total_fat, total_carbs, total_protein):
#     # Define the base nutrient requirements (as per 100g)
#     base_nutrients = {
#         'Carbs': 0,
#         'Total Fat': 0,
#         'Protein': 0,
#         'Calcium': 0,
#         'Cholesterol': 0,
#         'Fiber': 0,
#         'Iron': 0,
#         'Magnesium': 0
#     }

#     # Calculate the remaining nutrients based on the given total values
#     remaining_nutrients = base_nutrients.copy()
#     remaining_nutrients['Total Fat'] = total_fat
#     remaining_nutrients['Carbs'] = total_carbs
#     remaining_nutrients['Protein'] = total_protein

#     return remaining_nutrients

# # Define a function to recommend food items based on user requirements
# def recommend_food_items(user_requirements):
#     recommended_items = pd.DataFrame()

#     # Get user's nutritional requirements
#     total_fat = user_requirements['Total Fat']
#     total_carbs = user_requirements['Carbs']
#     total_protein = user_requirements['Protein']

#     remaining_nutrients = calculate_requirements(total_fat, total_carbs, total_protein)

#     cumulative_fat = 0
#     cumulative_carbs = 0
#     cumulative_protein = 0

#     for category in user_requirements['category']:
#         # Filter food items based on predicted categories and current category
#         filtered_food_items = combined_data[combined_data['Category'] == category]

#         # Shuffle the filtered items to get a random order
#         filtered_food_items = filtered_food_items.sample(frac=1).reset_index(drop=True)

#         for _, item in filtered_food_items.iterrows():
#             item_fat = item['Total Fat']
#             item_carbs = item['Carbs']
#             item_protein = item['Protein']

#             if (cumulative_fat + item_fat <= total_fat and
#                 cumulative_carbs + item_carbs <= total_carbs and
#                 cumulative_protein + item_protein <= total_protein):

#                 # Add the nutrients of the selected item to cumulative nutrients
#                 cumulative_fat += item_fat
#                 cumulative_carbs += item_carbs
#                 cumulative_protein += item_protein

#                 # Append the selected item to recommended items using concat
#                 recommended_items = pd.concat([recommended_items, pd.DataFrame([item])])

#                 # Stop if we reach the required amounts
#                 if (cumulative_fat >= total_fat and
#                     cumulative_carbs >= total_carbs and
#                     cumulative_protein >= total_protein):
#                     break

#         if (cumulative_fat >= total_fat and
#             cumulative_carbs >= total_carbs and
#             cumulative_protein >= total_protein):
#             break

#     return recommended_items

# # Example user requirements
# user_requirements = {
#     'Total Fat': 110,  # Example: 110 grams of fat
#     'Carbs': 300,  # Example: 300 grams of carbs
#     'Protein': 200,  # Example: 200 grams of protein
#     'category': ['Fruits', 'Grains', 'Vegetables', 'Meat', 'Protein']  # Example: List of categories
# }

# # Get recommended food items
# recommended_items = recommend_food_items(user_requirements)

# # Print recommended food items
# print("Recommended Food Items:")
# if not recommended_items.empty:
#     print(recommended_items)
#     # Print the total of selected nutrients
#     print("Total Nutrients of Selected Items:")
#     print(f"Total Fat: {recommended_items['Total Fat'].sum()} grams")
#     print(f"Carbs: {recommended_items['Carbs'].sum()} grams")
#     print(f"Protein: {recommended_items['Protein'].sum()} grams")
# else:
#     print("No items found matching the criteria.")

# # Dump the model
# joblib.dump(classifier, 'model.pkl')







import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load your data
final_foods = pd.read_csv("dataset/complete_food_items.csv")
calorie_value = pd.read_csv('dataset/Calorie_value.csv')

# Merge the data
combined_data = pd.merge(calorie_value, final_foods, on='food items')

# Define features and target
features = combined_data.drop(['Category', 'food items'], axis=1)  # Drop non-numeric columns
target = combined_data['Category']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=0)

# Initialize classifier
classifier = RandomForestClassifier()

# Fit the model
classifier.fit(X_train, y_train)

# Define a function to calculate remaining nutritional requirements
def calculate_requirements(total_fat, total_carbs, total_protein):
    # Define the base nutrient requirements (as per 100g)
    base_nutrients = {
        'Carbs': 0,
        'Total Fat': 0,
        'Protein': 0,
        'Calcium': 0,
        'Cholesterol': 0,
        'Fiber': 0,
        'Iron': 0,
        'Magnesium': 0
    }

    # Calculate the remaining nutrients based on the given total values
    remaining_nutrients = base_nutrients.copy()
    remaining_nutrients['Total Fat'] = total_fat
    remaining_nutrients['Carbs'] = total_carbs
    remaining_nutrients['Protein'] = total_protein

    return remaining_nutrients

# Define a function to recommend food items based on user requirements
def recommend_food_items(user_requirements):
    recommended_items = pd.DataFrame()

    # Get user's nutritional requirements
    total_fat = user_requirements['Total Fat']
    total_carbs = user_requirements['Carbs']
    total_protein = user_requirements['Protein']

    remaining_nutrients = calculate_requirements(total_fat, total_carbs, total_protein)

    cumulative_fat = 0
    cumulative_carbs = 0
    cumulative_protein = 0

    for category in user_requirements['category']:
        # Filter food items based on predicted categories and current category
        filtered_food_items = combined_data[combined_data['Category'] == category]

        if not filtered_food_items.empty:
            # Shuffle the filtered items to get a random order
            filtered_food_items = filtered_food_items.sample(frac=1).reset_index(drop=True)
            
            # Select at least one item from each category
            for _, item in filtered_food_items.iterrows():
                item_fat = item['Total Fat']
                item_carbs = item['Carbs']
                item_protein = item['Protein']

                # Add the nutrients of the selected item to cumulative nutrients
                cumulative_fat += item_fat
                cumulative_carbs += item_carbs
                cumulative_protein += item_protein

                # Append the selected item to recommended items using concat
                recommended_items = pd.concat([recommended_items, pd.DataFrame([item])])

                # Remove the selected item from the remaining nutrients
                remaining_nutrients['Total Fat'] -= item_fat
                remaining_nutrients['Carbs'] -= item_carbs
                remaining_nutrients['Protein'] -= item_protein

                break

    # Fill the remaining nutrient requirements
    for category in user_requirements['category']:
        filtered_food_items = combined_data[combined_data['Category'] == category]
        filtered_food_items = filtered_food_items.sample(frac=1).reset_index(drop=True)

        for _, item in filtered_food_items.iterrows():
            item_fat = item['Total Fat']
            item_carbs = item['Carbs']
            item_protein = item['Protein']

            if (cumulative_fat + item_fat <= total_fat and
                cumulative_carbs + item_carbs <= total_carbs and
                cumulative_protein + item_protein <= total_protein):

                cumulative_fat += item_fat
                cumulative_carbs += item_carbs
                cumulative_protein += item_protein

                recommended_items = pd.concat([recommended_items, pd.DataFrame([item])])

                if (cumulative_fat >= total_fat and
                    cumulative_carbs >= total_carbs and
                    cumulative_protein >= total_protein):
                    break

        if (cumulative_fat >= total_fat and
            cumulative_carbs >= total_carbs and
            cumulative_protein >= total_protein):
            break

    return recommended_items

# Example user requirements
user_requirements = {
    'Total Fat': 110,  # Example: 110 grams of fat
    'Carbs': 300,  # Example: 300 grams of carbs
    'Protein': 200,  # Example: 200 grams of protein
    'category': ['Fruits', 'Grains', 'Vegetables', 'Meat', 'Protein']  # Example: List of categories
}

# Get recommended food items
recommended_items = recommend_food_items(user_requirements)

# Print recommended food items
print("Recommended Food Items:")
if not recommended_items.empty:
    print(recommended_items)
    # Print the total of selected nutrients
    print("Total Nutrients of Selected Items:")
    print(f"Total Fat: {recommended_items['Total Fat'].sum()} grams")
    print(f"Carbs: {recommended_items['Carbs'].sum()} grams")
    print(f"Protein: {recommended_items['Protein'].sum()} grams")
else:
    print("No items found matching the criteria.")

# Dump the model
joblib.dump(classifier, 'model.pkl')

       













# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier

# # Load your data
# final_foods = pd.read_csv("dataset/complete_food_items.csv")
# calorie_value = pd.read_csv('dataset/Calorie_value.csv')

# # Merge the data
# combined_data = pd.merge(calorie_value, final_foods, on='food items')

# # Define features and target
# features = combined_data.drop(['Category', 'food items'], axis=1)  # Drop non-numeric columns
# target = combined_data['Category']

# # Split the data
# X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=0)

# # Initialize classifier
# classifier = RandomForestClassifier()

# # Fit the model
# classifier.fit(X_train, y_train)

# # Define a function to calculate remaining nutritional requirements
# def calculate_requirements(total_fat, total_carbs, total_protein):
#     # Define the base nutrient requirements (as per 100g)
#     base_nutrients = {
#         'Carbs': 0,
#         'Total Fat': 0,
#         'Protein': 0,
#         'Calcium': 0,
#         'Cholesterol': 0,
#         'Fiber': 0,
#         'Iron': 0,
#         'Magnesium': 0
#     }

#     # Calculate the remaining nutrients based on the given total values
#     remaining_nutrients = base_nutrients.copy()
#     remaining_nutrients['Total Fat'] = total_fat
#     remaining_nutrients['Carbs'] = total_carbs
#     remaining_nutrients['Protein'] = total_protein

#     return remaining_nutrients

# # Define a function to recommend food items based on user requirements
# def recommend_food_items(model, user_requirements):
#     recommended_items = pd.DataFrame()

#     # Get user's nutritional requirements
#     total_fat = user_requirements['Total Fat']
#     total_carbs = user_requirements['Carbs']
#     total_protein = user_requirements['Protein']

#     # Calculate the remaining nutrients based on the user's requirements
#     remaining_nutrients = calculate_requirements(total_fat, total_carbs, total_protein)

#     # Get user's categories
#     categories = user_requirements['category']

#     for category in categories:
#         # Filter food items based on predicted categories and current category
#         filtered_food_items = combined_data[(combined_data['Category'] == category)]

#         # Sample three random items from the filtered list, if available
#         if not filtered_food_items.empty:
#             sampled_items = filtered_food_items.sample(n=3)

#             for _, sampled_item in sampled_items.iterrows():
#                 # Get the nutrient values of the sampled item
#                 item_fat = sampled_item['Total Fat']
#                 item_carbs = sampled_item['Carbs']
#                 item_protein = sampled_item['Protein']

#                 # Check if adding this item exceeds the remaining nutrients
#                 if (remaining_nutrients['Total Fat'] - item_fat >= 0 and
#                     remaining_nutrients['Carbs'] - item_carbs >= 0 and
#                     remaining_nutrients['Protein'] - item_protein >= 0):

#                     # Subtract the nutrients of the selected item from remaining nutrients
#                     remaining_nutrients['Total Fat'] -= item_fat
#                     remaining_nutrients['Carbs'] -= item_carbs
#                     remaining_nutrients['Protein'] -= item_protein

#                     # Append the selected item to recommended items
#                     recommended_items = pd.concat([recommended_items, pd.DataFrame([sampled_item])])

#                     # Check if we have satisfied the requirement for this category
#                     if recommended_items['Category'].nunique() >= 3:
#                         break

#         # Check if we have satisfied the requirement for all categories
#         if recommended_items['Category'].nunique() >= 3:
#             break

#     return recommended_items

# # Example user requirements
# user_requirements = {
#     'Total Fat': 110,  # Example: 110 grams of fat
#     'Carbs': 300,  # Example: 300 grams of carbs
#     'Protein': 200,  # Example: 200 grams of protein
#     'category': ['Fruit', 'Grains']  # Example: List of categories
# }

# # Get recommended food items
# recommended_items = recommend_food_items(classifier, user_requirements)

# # Print recommended food items
# print("Recommended Food Items:")
# if not recommended_items.empty:
#     print(recommended_items[['food items', 'Category']])
# else:
#     print("No items found matching the criteria.")
