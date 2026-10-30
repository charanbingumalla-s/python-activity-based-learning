# Student Email and Identifier Validation System

import re


def validate_email(email):
    errors = []

    # Check for missing email
    if not email:
        errors.append("Missing email address")
        return errors

    # Check for spaces
    if " " in email:
        errors.append("Email must not contain spaces")

    # Check for missing or multiple @ symbols
    if email.count("@") == 0:
        errors.append("Missing @ symbol")
        return errors

    if email.count("@") > 1:
        errors.append("Multiple @ symbols found")
        return errors

    # Separate the username and domain
    username, domain = email.split("@")

    # Check for missing components
    if not username:
        errors.append("Missing username")

    if not domain:
        errors.append("Missing domain")
        return errors

    # Check username formatting
    if username.startswith(".") or username.endswith("."):
        errors.append("Username cannot start or end with a dot")

    if ".." in username:
        errors.append("Consecutive dots in username")

    if not re.fullmatch(r"[A-Za-z0-9._+-]+", username):
        errors.append("Invalid character in username")

    # Check domain formatting
    if domain.startswith(".") or domain.endswith("."):
        errors.append("Domain cannot start or end with a dot")

    if ".." in domain:
        errors.append("Consecutive dots in domain")

    if "." not in domain:
        errors.append("Domain must contain a dot")

    # Check domain labels
    labels = domain.split(".")

    for label in labels:
        if not label:
            errors.append("Missing domain component")
            break

        if label.startswith("-") or label.endswith("-"):
            errors.append(
                "Domain components cannot start or end with a hyphen"
            )

        if not re.fullmatch(r"[A-Za-z0-9-]+", label):
            errors.append("Invalid character in domain")

    # Check final domain component
    if labels and labels[-1]:
        if not re.fullmatch(r"[A-Za-z]{2,}", labels[-1]):
            errors.append(
                "Final domain component must contain at least "
                "two letters"
            )

    return errors


def validate_registration_id(registration_id):
    errors = []

    # Example registration ID format: 24CSE1234
    # Rules:
    # 1. Two digits for admission year
    # 2. Three uppercase letters for department
    # 3. Four digits for student number

    if not registration_id:
        errors.append("Missing registration identifier")
        return errors

    if " " in registration_id:
        errors.append("Registration ID must not contain spaces")

    if registration_id.count("-") > 0:
        errors.append("Hyphens are not allowed")

    if registration_id.count("_") > 0:
        errors.append("Underscores are not allowed")

    if len(registration_id) < 9:
        errors.append("Registration ID is missing characters")
    elif len(registration_id) > 9:
        errors.append("Registration ID contains extra characters")

    if len(registration_id) >= 2:
        year = registration_id[:2]

        if not year.isdigit():
            errors.append(
                "Admission year must contain exactly two digits"
            )

    if len(registration_id) >= 5:
        department = registration_id[2:5]

        if not department.isalpha():
            errors.append(
                "Department must contain three letters"
            )
        elif not department.isupper():
            errors.append(
                "Department letters must be uppercase"
            )

    if len(registration_id) >= 9:
        student_number = registration_id[5:9]

        if not student_number.isdigit():
            errors.append(
                "Student number must contain four digits"
            )

    # Check for characters outside letters and digits
    if not re.fullmatch(r"[A-Za-z0-9]+", registration_id):
        errors.append(
            "Registration ID contains invalid characters"
        )

    return errors


def display_result(label, value, errors):
    print(f"\n{label}: {value}")

    if not errors:
        print("Status: VALID")
    else:
        print("Status: INVALID")
        for error in errors:
            print(f"- {error}")


def main():
    print("=" * 55)
    print("     STUDENT EMAIL AND IDENTIFIER VALIDATION")
    print("=" * 55)

    while True:
        print("\n1. Validate student email")
        print("2. Validate registration ID")
        print("3. Validate both")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            email = input("Enter student email: ").strip()
            errors = validate_email(email)
            display_result("Email", email, errors)

        elif choice == "2":
            registration_id = input(
                "Enter registration ID: "
            ).strip()

            errors = validate_registration_id(registration_id)
            display_result(
                "Registration ID",
                registration_id,
                errors
            )

        elif choice == "3":
            email = input("Enter student email: ").strip()
            registration_id = input(
                "Enter registration ID: "
            ).strip()

            email_errors = validate_email(email)
            id_errors = validate_registration_id(registration_id)

            display_result("Email", email, email_errors)
            display_result(
                "Registration ID",
                registration_id,
                id_errors
            )

        elif choice == "4":
            print("Exiting validation system. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
