import pandas as pd

def load_flight_data(file_path):
    """Load flight data from a CSV file"""
    return pd.read_csv(file_path)

def get_data_shape(data):
    return data.shape