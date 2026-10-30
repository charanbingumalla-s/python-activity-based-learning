# Railway Fare and Reservation Calculator

# Illustrative fare rates per kilometre
FARE_RATES = {
    "Sleeper": 1.0,
    "AC3": 2.0,
    "AC2": 3.0,
    "AC1": 4.0
}

# Reservation fees per passenger
RESERVATION_FEES = {
    "Sleeper": 20,
    "AC3": 40,
    "AC2": 50,
    "AC1": 60
}

# Illustrative age-based concessions
CHILD_AGE_LIMIT = 12
SENIOR_AGE_LIMIT = 60
CHILD_CONCESSION = 0.50
SENIOR_CONCESSION = 0.40

# Illustrative cancellation penalty percentages
CANCELLATION_PENALTIES = {
    "Sleeper": 0.10,
    "AC3": 0.15,
    "AC2": 0.20,
    "AC1": 0.25
}


# Calculate fare for one passenger
def calculate_fare(distance, travel_class, age):

    base_fare = distance * FARE_RATES[travel_class]

    concession = 0

    if age < CHILD_AGE_LIMIT:
        concession = base_fare * CHILD_CONCESSION

    elif age >= SENIOR_AGE_LIMIT:
        concession = base_fare * SENIOR_CONCESSION

    discounted_fare = base_fare - concession

    reservation_fee = RESERVATION_FEES[travel_class]

    total_fare = discounted_fare + reservation_fee

    return {
        "base_fare": base_fare,
        "concession": concession,
        "reservation_fee": reservation_fee,
        "total_fare": total_fare
    }


# Calculate cancellation refund
def calculate_cancellation(total_fare, travel_class):

    penalty_rate = CANCELLATION_PENALTIES[travel_class]

    cancellation_penalty = total_fare * penalty_rate

    refund = total_fare - cancellation_penalty

    return cancellation_penalty, refund


# Get valid positive number
def get_positive_number(message):

    while True:
        try:
            value = float(input(message))

            if value > 0:
                return value

            print("Please enter a number greater than zero.")

        except ValueError:
            print("Invalid input. Please enter a number.")


# Main program
def main():

    print("=" * 45)
    print(" RAILWAY FARE AND RESERVATION CALCULATOR")
    print("=" * 45)

    distance = get_positive_number(
        "Enter journey distance in kilometres: "
    )

    print("\nAvailable Travel Classes:")
    print("1. Sleeper")
    print("2. AC3")
    print("3. AC2")
    print("4. AC1")

    class_options = {
        "1": "Sleeper",
        "2": "AC3",
        "3": "AC2",
        "4": "AC1"
    }

    while True:
        choice = input("Select travel class (1-4): ").strip()

        if choice in class_options:
            travel_class = class_options[choice]
            break

        print("Invalid choice. Please select 1, 2, 3, or 4.")

    passenger_count = int(
        get_positive_number("Enter number of passengers: ")
    )

    passengers = []
    grand_total = 0

    # Enter passenger details
    for i in range(passenger_count):

        print(f"\nPassenger {i + 1}")

        while True:
            name = input("Enter passenger name: ").strip()

            if name:
                break

            print("Name cannot be empty.")

        while True:
            try:
                age = int(input("Enter passenger age: "))

                if 0 <= age <= 120:
                    break

                print("Enter an age between 0 and 120.")

            except ValueError:
                print("Please enter a valid whole number.")

        fare_details = calculate_fare(
            distance, travel_class, age
        )

        passengers.append({
            "name": name,
            "age": age,
            "fare": fare_details
        })

        grand_total += fare_details["total_fare"]

    # Display reservation details
    print("\n" + "=" * 45)
    print("           RESERVATION SUMMARY")
    print("=" * 45)

    print(f"Distance: {distance:g} km")
    print(f"Travel Class: {travel_class}")
    print(f"Number of Passengers: {passenger_count}")

    for i, passenger in enumerate(passengers, start=1):

        fare = passenger["fare"]

        print(f"\nPassenger {i}: {passenger['name']}")
        print(f"Age: {passenger['age']}")
        print(f"Base Fare: Rs. {fare['base_fare']:.2f}")
        print(f"Age Concession: Rs. {fare['concession']:.2f}")
        print(
            f"Reservation Fee: Rs. "
            f"{fare['reservation_fee']:.2f}"
        )
        print(f"Total Fare: Rs. {fare['total_fare']:.2f}")

    print("\n" + "-" * 45)
    print(f"TOTAL RESERVATION FARE: Rs. {grand_total:.2f}")
    print("-" * 45)

    # Cancellation calculation
    cancel = input(
        "\nWould you like to calculate cancellation charges? (yes/no): "
    ).strip().lower()

    if cancel == "yes":

        penalty, refund = calculate_cancellation(
            grand_total, travel_class
        )

        print("\n" + "=" * 45)
        print("          CANCELLATION SUMMARY")
        print("=" * 45)

        print(f"Original Fare: Rs. {grand_total:.2f}")
        print(f"Cancellation Penalty: Rs. {penalty:.2f}")
        print(f"Refund Amount: Rs. {refund:.2f}")

    print("\nThank you for using the Railway Calculator!")


if __name__ == "__main__":
    main()