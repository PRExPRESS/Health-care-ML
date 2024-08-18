from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import numpy as np  # For numerical operations
import joblib  # For loading the trained model
from finalFoodItems import calculate_requirements, recommend_food_items, filter_diesease, filter_meal_time, filter_food, filter_by_category
from calculation import req_food,mealtime_calculation,calculate_bmr, calculate_calories, calculate_dieseas_nutrion_level, calculate_nutrition, max_breakfast, max_lunch, max_snack, max_dinner, recommended_items
from input import filter_food, filter_meal_time
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})


model = joblib.load('model.pkl') 

@app.route('/api/recommend_diet_plan', methods=['POST'])
def get_foods_by_user_request():
    try:
        data = request.get_json()

        weight_s = data.get('weight')
        height_s = data.get('height')
        age_s = data.get('age')
        gender = data.get('gender')
        diease = data.get('diease')
        mealtime = data.get('mealtime')
        foodtype = data.get('foodtype')

        weight = int(weight_s)
        height = int(height_s)
        age = int(age_s)

        print(data)
        bmr = calculate_bmr(weight,height,age,gender)
        calories = calculate_calories(bmr)
        nutrion_level = calculate_dieseas_nutrion_level(diease)
        nutrition = calculate_nutrition(calories,nutrion_level)
        mealtime_nutrition = mealtime_calculation(mealtime,nutrition)
        req_foodtype = req_food(foodtype)
        
        user_require = {
            'Carbs': list(mealtime_nutrition)[0],  
            'Total Fat': list(mealtime_nutrition)[1], 
            'Protein': list(mealtime_nutrition)[2],  
            'Calories': calories, 
            'category': req_foodtype  
        }

        predict = recommend_food_items(user_require)

        d = predict.columns[predict.columns.duplicated()]
        if d.empty:
          filtered_items = predict[['food items', 'Total Fat','Protein','Carbs']]
          reset = filtered_items.reset_index(drop=True)
          json_data = reset.to_json()
          return json_data
        else:
            print("duplicated")  

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 400
    
@app.route('/api/recommend_diet_plan/types', methods=['POST'])
def get_foods_by_type():
    try:
        data = request.get_json()
        filter_foods = filter_by_category(data)
        food_items = filter_foods["food items"].to_json()
        return food_items

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 400

# Example endpoint to get diet plan recommendations
@app.route('/api/recommend_diet', methods=['POST'])
def recommend_diet_plan():
    try:
        # Assume your model expects certain features in the request
        data = request.get_json()

        # Example: Convert data to features
        features = preprocess_data(data)  # Implement your own preprocessing function

        # Make prediction using your model
        prediction = model.predict(features)

        # Example response
        response = {
            'diet_plan': prediction.tolist()  # Convert to list if necessary
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Example preprocessing function (replace with your own preprocessing logic)
def preprocess_data(data):
    # Example: Extract features from data
    features = np.array([data['feature1'], data['feature2']])  # Replace with your feature extraction logic
    return features










if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1', port=5000)