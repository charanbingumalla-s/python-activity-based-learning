# University Scholarship Allocation System

# Eligibility criteria
MIN_AGGREGATE = 75
MIN_SUBJECT_MARKS = 60
MIN_ATTENDANCE = 75
MAX_FAMILY_INCOME = 300000

# Student records
students = [
    {
        "name": "Rahul",
        "aggregate": 90,
        "subjects": [85, 92, 88],
        "attendance": 90,
        "income": 200000
    },
    {
        "name": "Priya",
        "aggregate": 95,
        "subjects": [90, 95, 92],
        "attendance": 85,
        "income": 250000
    },
    {
        "name": "Arun",
        "aggregate": 80,
        "subjects": [65, 70, 75],
        "attendance": 80,
        "income": 180000
    },
    {
        "name": "Sneha",
        "aggregate": 90,
        "subjects": [55, 90, 85],
        "attendance": 95,
        "income": 150000
    },
    {
        "name": "Kiran",
        "aggregate": 90,
        "subjects": [80, 85, 90],
        "attendance": 90,
        "income": 150000
    }
]


# Check scholarship eligibility
def check_eligibility(student):

    if student["aggregate"] < MIN_AGGREGATE:
        return False

    if any(mark < MIN_SUBJECT_MARKS
           for mark in student["subjects"]):
        return False

    if student["attendance"] < MIN_ATTENDANCE:
        return False

    if student["income"] > MAX_FAMILY_INCOME:
        return False

    return True


# Separate eligible and ineligible students
eligible_students = []
ineligible_students = []

for student in students:
    if check_eligibility(student):
        eligible_students.append(student)
    else:
        ineligible_students.append(student)


# Rank eligible students
# Tie-breaking rules:
# 1. Higher aggregate marks
# 2. Higher attendance
# 3. Lower family income
# 4. Alphabetical order of name

eligible_students.sort(
    key=lambda student: (
        -student["aggregate"],
        -student["attendance"],
        student["income"],
        student["name"].lower()
    )
)


# Display eligible students
print("\n===== SCHOLARSHIP MERIT LIST =====")

if eligible_students:
    for rank, student in enumerate(eligible_students, start=1):
        print(f"\nRank: {rank}")
        print(f"Name: {student['name']}")
        print(f"Aggregate: {student['aggregate']}%")
        print(f"Subject Marks: {student['subjects']}")
        print(f"Attendance: {student['attendance']}%")
        print(f"Family Income: Rs. {student['income']}")
        print("Status: ELIGIBLE")
else:
    print("No eligible students found.")


# Display ineligible students
print("\n===== INELIGIBLE STUDENTS =====")

if ineligible_students:
    for student in ineligible_students:
        print(f"\nName: {student['name']}")
        print("Status: INELIGIBLE")

        if student["aggregate"] < MIN_AGGREGATE:
            print("Reason: Aggregate marks below minimum.")

        if any(mark < MIN_SUBJECT_MARKS
               for mark in student["subjects"]):
            print("Reason: Minimum subject marks not satisfied.")

        if student["attendance"] < MIN_ATTENDANCE:
            print("Reason: Attendance below minimum.")

        if student["income"] > MAX_FAMILY_INCOME:
            print("Reason: Family income exceeds the limit.")
else:
    print("All students are eligible.")