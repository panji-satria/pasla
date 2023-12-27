# pemrosesan.py
import numpy as np

def preprocess_data(data):
    processed_data = np.log(data + 1)
    print("Data preprocessed successfully.")
    return processed_data
