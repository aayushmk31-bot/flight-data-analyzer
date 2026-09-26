import requests
import pandas as pd

def load_flight_data(file_path):
    """Load flight data from a CSV file"""
    return pd.read_csv(file_path)

def get_data_shape(data):
    return data.shape

def get_aircraft_data():
    url="https://opensky-network.org/api/states/all"

    params={
        "lamin": 12.930,
        "lomin": 77.430,
        "lamax": 13.468,
        "lomax": 77.982,
    }

    response = requests.get(url, params=params)

    response.raise_for_status()

    data = response.json()

    columns=[
        "icao24",
        "callsign",
        "country",
        "time_position",
        "last_contact",
        "longitude",
        "latitude",
        "baro_altitude",
        "on_ground",
        "velocity",
        "heading",
        "vertical_rate",
        "sensors",
        "geo_altitude",
        "squawk",
        "spi",
        "position_source",
    ]

    return pd.DataFrame(data["states"], columns=columns)
