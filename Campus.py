# Campus Event Financial Planning System

import math

# Calculate total event expenses
def calculate_expenses(venue, equipment, catering, transport, certificates):
    return venue + equipment + catering + transport + certificates


# Calculate participant contribution
def calculate_contribution(total_expenses, sponsorship, participants):
    remaining_amount = max(0, total_expenses - sponsorship)

    if participants <= 0:
        return 0

    return remaining_amount / participants


# Calculate sponsorship shortfall
def calculate_shortfall(total_expenses, sponsorship, registration_fee, participants):
    registration_income = registration_fee * participants
    total_funding = sponsorship + registration_income

    return max(0, total_expenses - total_funding)


# Calculate minimum registrations needed to break even
def calculate_break_even(total_expenses, sponsorship, registration_fee):
    if registration_fee <= 0:
        return None

    remaining_amount = max(0, total_expenses - sponsorship)

    return math.ceil(remaining_amount / registration_fee)


# Get valid non-negative amount
def get_amount(message):
    while True:
        try:
            amount = float(input(message))

            if amount < 0:
                print("Amount cannot be negative.")
            else:
                return amount

        except ValueError:
            print("Please enter a valid number.")


# Get valid positive integer
def get_positive_integer(message):
    while True:
        try:
            number = int(input(message))

            if number > 0:
                return number

            print("Please enter a number greater than zero.")

        except ValueError:
            print("Please enter a valid whole number.")


# Main program
def main():

    print("=" * 50)
    print(" CAMPUS EVENT FINANCIAL PLANNING SYSTEM")
    print("=" * 50)

    # Collect event expenses
    print("\nEnter Event Expenses")

    venue = get_amount("Venue cost (Rs.): ")
    equipment = get_amount("Equipment cost (Rs.): ")
    catering = get_amount("Catering cost (Rs.): ")
    transport = get_amount("Transport cost (Rs.): ")
    certificates = get_amount("Certificate cost (Rs.): ")

    total_expenses = calculate_expenses(
        venue, equipment, catering, transport, certificates
    )

    print(f"\nTotal Event Expenses: Rs. {total_expenses:.2f}")

    # Collect sponsorship and registration details
    print("\nEnter Funding Details")

    sponsorship = get_amount("Available sponsorship (Rs.): ")
    registration_fee = get_amount("Registration fee per participant (Rs.): ")
    participants = get_positive_integer("Expected number of participants: ")

    # Calculate participant contribution
    contribution = calculate_contribution(
        total_expenses, sponsorship, participants
    )

    # Calculate sponsorship shortfall
    shortfall = calculate_shortfall(
        total_expenses, sponsorship, registration_fee, participants
    )

    # Calculate break-even registrations
    break_even = calculate_break_even(
        total_expenses, sponsorship, registration_fee
    )

    # Calculate total expected revenue
    registration_income = registration_fee * participants
    total_funding = sponsorship + registration_income
    surplus = max(0, total_funding - total_expenses)

    # Display financial report
    print("\n" + "=" * 50)
    print("             EVENT FINANCIAL REPORT")
    print("=" * 50)

    print(f"Venue Cost:              Rs. {venue:.2f}")
    print(f"Equipment Cost:          Rs. {equipment:.2f}")
    print(f"Catering Cost:           Rs. {catering:.2f}")
    print(f"Transport Cost:          Rs. {transport:.2f}")
    print(f"Certificate Cost:        Rs. {certificates:.2f}")

    print("-" * 50)
    print(f"Total Expenses:          Rs. {total_expenses:.2f}")
    print(f"Sponsorship:             Rs. {sponsorship:.2f}")
    print(f"Registration Income:     Rs. {registration_income:.2f}")
    print(f"Total Available Funding: Rs. {total_funding:.2f}")

    print("-" * 50)
    print(f"Contribution Per Person: Rs. {contribution:.2f}")
    print(f"Funding Shortfall:       Rs. {shortfall:.2f}")

    if break_even is None:
        print("Break-Even Registrations: Cannot be reached with a zero fee.")
    else:
        print(f"Break-Even Registrations: {break_even}")

    if shortfall == 0:
        print("\nStatus: EVENT IS FULLY FUNDED.")

        if surplus > 0:
            print(f"Expected Surplus: Rs. {surplus:.2f}")
        else:
            print("The event breaks even exactly.")

    else:
        print("\nStatus: ADDITIONAL FUNDING IS REQUIRED.")
        print(f"Additional Amount Needed: Rs. {shortfall:.2f}")

    print("=" * 50)
    print("Financial planning completed successfully.")


if __name__ == "__main__":
    main()