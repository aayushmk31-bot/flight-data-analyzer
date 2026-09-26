def calculate_climb_rate(data):
    altitude_change=data["altitude"].iloc[-1] - data["altitude"].iloc[0]
    time_change=data["time"].iloc[-1] - data["time"].iloc[0]

    climb_rate=altitude_change/(time_change/60)
    
    return climb_rate
    