import pandas as pd
import json
import joblib


data = pd.read_csv('dataset\diseases.csv')

def filter_diesease(diesease):
    filtered_data = data[data["Disease"] == diesease]
    return filtered_data

