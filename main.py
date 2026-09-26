from src.data_loader import load_flight_data, get_data_shape
from src.calculations import calculate_climb_rate
from src.data_loader import get_aircraft_data

data=load_flight_data("test_flight.csv")

def show_menu():
    print("\n" + "=" * 40)
    print("       FLIGHT DATA ANALYZER")
    print("=" * 40)
    print("1. View test dataset")
    print("2. Dataset information")
    print("3. Flight statistics")
    print("4. Calculate climb rate")
    print("5. Fetch live aircraft")
    print("6. Analyze Vertical Movement")
    print("7. Exit")
while True: 
    show_menu()
    choice=input("Enter your choice (1-7): ")

    print("You Selected Option:", choice)

    if choice=='1':
        print("\nFlight Dataset")
        print(data)

    elif choice == "2":
        print("\nDataset Information")
        print("-" * 30)
        data.info()

    elif choice == "3":
        print("\nFlight Statistics")
        print("-" * 30)
        print("Maximum altitude:", data["altitude"].max())
        print("Average altitude:", data["altitude"].mean())
        print("Maximum speed:", data["speed"].max())

    elif choice=='4':
        print("\nClimb Rate Calculation")
        climb_rate = calculate_climb_rate(data)
        print('-' * 30)
        print("Climb Rate:", climb_rate)

    elif choice == "5":
        aircraft_data = get_aircraft_data()
        print("\nOpenSky Aircraft Data")
        print("-" * 30)
        print("\nLive Aircraft Data")
        print("Aircraft Detected: ", len(aircraft_data))
        airborne=aircraft_data[aircraft_data['on_ground'] == False]
        airborne_altitudes = airborne["baro_altitude"].dropna()
        ground=aircraft_data[aircraft_data['on_ground'] == True]
        unknown=aircraft_data[aircraft_data['on_ground'].isna()]
        print("No. of Airborne Aircraft: ", len(airborne))
        print("No. of Aircraft on Ground: ", len(ground))
        print("No. of Aircraft with Unknown Status: ", len(unknown))
        if len(airborne_altitudes) > 0:
            print("Highest altitude:", round(airborne_altitudes.max()*3.28084), "ft")
            print("Lowest altitude:", round(airborne_altitudes.min()*3.28084), "ft")
            print("Average altitude:", round(airborne_altitudes.mean()*3.28084), "ft")
        else:
            print("No altitude data available.")

    elif choice == "6":
        print("\nVertical Movement Analysis")
        print("-" * 30)
        aircraft_data=get_aircraft_data()
        airborne=aircraft_data[aircraft_data['on_ground'] == False]
        if len(airborne) > 0:
            vertical_movements = airborne["vertical_rate"].dropna()
            climbing = vertical_movements[vertical_movements > 0]
            descending = vertical_movements[vertical_movements < 0]
            level = vertical_movements[vertical_movements == 0]
            print("Number of Aircraft Climbing:", len(climbing))
            print("Number of Aircraft Descending:", len(descending))
            print("Number of Aircraft Level:", len(level))

    elif choice == "7":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option (1-7)")


