def ClimbRate(data):
    altitude_change=data["altitude"].iloc[-1] - data["altitude"].iloc[0]
    print("Altitude change:", altitude_change)
    time_change=data["time"].iloc[-1] - data["time"].iloc[0]
    print("Time change:", time_change)
    climb_rate=altitude_change/(time_change/60)
    print("Climb Rate:", climb_rate, "ft/min")