# Campus Registration Identifier Analyzer

import re


# Branch codes and their names
BRANCHES = {
    "CSE": "Computer Science and Engineering",
    "ECE": "Electronics and Communication Engineering",
    "EEE": "Electrical and Electronics Engineering",
    "ME": "Mechanical Engineering",
    "CE": "Civil Engineering",
    "IT": "Information Technology",
    "AIM": "Artificial Intelligence and Machine Learning"
}


def analyze_identifier(identifier):
    identifier = identifier.strip().upper()

    # Example format: 24CSE1234
    # 24   = Admission year code
    # CSE  = Branch code
    # 1234 = Student number

    result = {
        "identifier": identifier,
        "valid": False,
        "year_code": None,
        "branch_code": None,
        "branch_name": None,
        "student_number": None,
        "errors": []
    }

    if not identifier:
        result["errors"].append("Identifier is missing")
        return result

    # Check the general structure:
    # Two digits + 2 or 3 uppercase letters + four digits
    match = re.fullmatch(r"(\d{2})([A-Z]{2,3})(\d{4})", identifier)

    if not match:
        result["errors"].append(
            "Invalid structure. Expected format: YYBBBNNNN "
            "(for example, 24CSE1234)"
        )
        return result

    year_code, branch_code, student_number = match.groups()

    result["year_code"] = year_code
    result["branch_code"] = branch_code
    result["student_number"] = student_number

    # Check whether the branch code is recognized
    if branch_code not in BRANCHES:
        result["errors"].append("Unknown branch code")

    # Check admission year code
    year_number = int(year_code)

    if year_number < 20 or year_number > 30:
        result["errors"].append(
            "Admission year code must be between 20 and 30"
        )

    # Set branch name if the branch is recognized
    if branch_code in BRANCHES:
        result["branch_name"] = BRANCHES[branch_code]

    # Valid only if no errors were found
    result["valid"] = len(result["errors"]) == 0

    return result


def classify_records(records):
    branch_groups = {}
    year_groups = {}

    for record in records:
        if not record["valid"]:
            continue

        branch = record["branch_code"]
        year = record["year_code"]

        branch_groups.setdefault(branch, []).append(record)
        year_groups.setdefault(year, []).append(record)

    return branch_groups, year_groups


def display_record(record):
    print("\n" + "-" * 50)
    print("Registration ID:", record["identifier"])

    if record["valid"]:
        print("Status: VALID")
        print("Admission Year Code:", record["year_code"])
        print("Branch Code:", record["branch_code"])
        print("Branch Name:", record["branch_name"])
        print("Student Number:", record["student_number"])
    else:
        print("Status: INVALID")
        for error in record["errors"]:
            print("Error:", error)


def display_classification(records):
    branch_groups, year_groups = classify_records(records)

    print("\n" + "=" * 60)
    print("           CLASSIFICATION BY BRANCH")
    print("=" * 60)

    if not branch_groups:
        print("No valid records available for classification.")

    for branch, group in sorted(branch_groups.items()):
        print(f"\n{branch} - {BRANCHES[branch]}")
        print("Number of students:", len(group))

        for record in group:
            print(" ", record["identifier"])

    print("\n" + "=" * 60)
    print("        CLASSIFICATION BY ADMISSION YEAR")
    print("=" * 60)

    if not year_groups:
        print("No valid records available for classification.")

    for year, group in sorted(year_groups.items()):
        print(f"\nAdmission Year Code: {year}")
        print("Number of students:", len(group))

        for record in group:
            print(" ", record["identifier"])

    print("\n" + "=" * 60)


def main():
    print("=" * 60)
    print("       CAMPUS REGISTRATION IDENTIFIER ANALYZER")
    print("=" * 60)

    records = []

    try:
        number = int(input("Enter the number of student records: "))

        if number <= 0:
            print("Please enter a number greater than zero.")
            return

        for i in range(number):
            print(f"\nEnter details for Student {i + 1}")

            identifier = input("Registration ID: ")
            record = analyze_identifier(identifier)

            records.append(record)
            display_record(record)

        display_classification(records)

        valid_count = sum(1 for record in records if record["valid"])
        invalid_count = len(records) - valid_count

        print("\nFINAL SUMMARY")
        print("-" * 30)
        print("Total records:", len(records))
        print("Valid records:", valid_count)
        print("Invalid records:", invalid_count)

    except ValueError:
        print("Invalid input. Enter a whole number for the record count.")


if __name__ == "__main__":
    main()
