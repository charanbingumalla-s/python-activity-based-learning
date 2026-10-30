# Hospital Billing and Patient Classification System

# Billing rates
CONSULTATION_FEE = 500
DIAGNOSTIC_FEE = 1000
TREATMENT_FEE = 2000

# Concession percentages
SENIOR_CONCESSION = 0.10
LOW_INCOME_CONCESSION = 0.15
MAX_CONCESSION = 0.25

# Payment classification limits
LOW_BILL_LIMIT = 2000
MEDIUM_BILL_LIMIT = 5000

# Maximum allowed charges
MAX_BILL_AMOUNT = 100000


# Calculate hospital bill
def calculate_bill(consultation, diagnostic, treatment,
                   age, low_income):

    subtotal = consultation + diagnostic + treatment

    concession_rate = 0

    # Apply senior citizen concession
    if age >= 60:
        concession_rate += SENIOR_CONCESSION

    # Apply low-income concession
    if low_income:
        concession_rate += LOW_INCOME_CONCESSION

    # Limit total concession
    concession_rate = min(concession_rate, MAX_CONCESSION)

    concession = subtotal * concession_rate

    total = subtotal - concession

    return {
        "consultation": consultation,
        "diagnostic": diagnostic,
        "treatment": treatment,
        "subtotal": subtotal,
        "concession_rate": concession_rate,
        "concession": concession,
        "total": total
    }


# Validate billing information
def validate_bill(consultation, diagnostic, treatment, age):

    if consultation < 0 or diagnostic < 0 or treatment < 0:
        return False, "Charges cannot be negative."

    if age < 0 or age > 120:
        return False, "Age must be between 0 and 120."

    subtotal = consultation + diagnostic + treatment

    if subtotal > MAX_BILL_AMOUNT:
        return False, "Bill exceeds the maximum allowed amount."

    if subtotal == 0:
        return False, "Total bill must be greater than zero."

    return True, "Billing information is valid."


# Classify patient according to final bill
def classify_patient(total):

    if total <= LOW_BILL_LIMIT:
        return "Category A - Low Payment"

    elif total <= MEDIUM_BILL_LIMIT:
        return "Category B - Medium Payment"

    else:
        return "Category C - High Payment"


# Get a valid non-negative charge
def get_charge(message):

    while True:
        try:
            amount = float(input(message))

            if amount < 0:
                print("Charge cannot be negative.")
            else:
                return amount

        except ValueError:
            print("Please enter a valid amount.")


# Get valid age
def get_age():

    while True:
        try:
            age = int(input("Enter patient age: "))

            if 0 <= age <= 120:
                return age

            print("Age must be between 0 and 120.")

        except ValueError:
            print("Please enter a valid whole number.")


# Main program
def main():

    print("=" * 45)
    print(" HOSPITAL BILLING AND PATIENT CLASSIFICATION")
    print("=" * 45)

    patient_name = input("Enter patient name: ").strip()

    while not patient_name:
        print("Patient name cannot be empty.")
        patient_name = input("Enter patient name: ").strip()

    age = get_age()

    print("\nEnter consultation, diagnostic, and treatment charges.")

    consultation = get_charge("Consultation charges: Rs. ")
    diagnostic = get_charge("Diagnostic charges: Rs. ")
    treatment = get_charge("Treatment charges: Rs. ")

    low_income_input = input(
        "Is the patient eligible for the low-income concession? (yes/no): "
    ).strip().lower()

    while low_income_input not in ("yes", "no"):
        print("Please enter yes or no.")
        low_income_input = input(
            "Is the patient eligible for the low-income concession? (yes/no): "
        ).strip().lower()

    low_income = low_income_input == "yes"

    # Validate billing information
    valid, message = validate_bill(
        consultation, diagnostic, treatment, age
    )

    if not valid:
        print("\nBilling Error:", message)
        return

    # Calculate bill
    bill = calculate_bill(
        consultation, diagnostic, treatment, age, low_income
    )

    # Classify patient
    category = classify_patient(bill["total"])

    # Display bill
    print("\n" + "=" * 45)
    print("             HOSPITAL BILL")
    print("=" * 45)

    print("Patient Name:", patient_name)
    print("Patient Age:", age)

    print("-" * 45)
    print(f"Consultation Charges: Rs. {bill['consultation']:.2f}")
    print(f"Diagnostic Charges:   Rs. {bill['diagnostic']:.2f}")
    print(f"Treatment Charges:    Rs. {bill['treatment']:.2f}")

    print("-" * 45)
    print(f"Subtotal:             Rs. {bill['subtotal']:.2f}")
    print(f"Concession Rate:      {bill['concession_rate'] * 100:.0f}%")
    print(f"Concession Amount:    Rs. {bill['concession']:.2f}")
    print(f"Final Bill:           Rs. {bill['total']:.2f}")

    print("-" * 45)
    print("Patient Classification:", category)
    print("=" * 45)

    print("Billing completed successfully.")


# Run the program
if __name__ == "__main__":
    main()