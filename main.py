from src.data_loader import load_flight_data, get_data_shape


data = load_flight_data("test_flight.csv")

print(data)
print()

print("Dataset dimensions:", get_data_shape(data))
print()

print("First 5 Rows")
print(data.head(5))

print("Dataset Information")
print(data.info())

print("Maximum altitude:", data['altitude'].max())
print("Average altitude:", data['altitude'].mean())
print("Maximum Speed: ", data['speed'].max())

altitude_change=data["altitude"].iloc[-1] - data["altitude"].iloc[0]
print("Altitude change:", altitude_change)
time_change=data["time"].iloc[-1] - data["time"].iloc[0]
print("Time change:", time_change)
climb_rate=altitude_change/(time_change/60)
print("Climb Rate:", climb_rate, "ft/min")