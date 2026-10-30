# Nested List Classroom Occupancy Analysis

def create_classrooms():
    # Each classroom is represented as a nested list.
    # None = vacant seat
    # "RESERVED" = seat reserved and unavailable for allocation
    classrooms = {
        "Room A": [
            [None, None, "RESERVED", None],
            [None, None, None, None],
            [None, "RESERVED", None, None]
        ],
        "Room B": [
            [None, None, None],
            ["RESERVED", None, None],
            [None, None, None]
        ],
        "Room C": [
            [None, "RESERVED", None, None],
            [None, None, None, None]
        ]
    }

    return classrooms


def find_student(classrooms, student_name):
    # Search all classrooms for an existing student.
    for room_name, rows in classrooms.items():
        for row_index, row in enumerate(rows):
            for seat_index, seat in enumerate(row):
                if seat == student_name:
                    return room_name, row_index, seat_index

    return None


def allocate_student(classrooms, student_name, room_name):
    if not student_name.strip():
        return "ERROR: Student name cannot be empty."

    student_name = student_name.strip()

    # Prevent duplicate assignments.
    existing_seat = find_student(classrooms, student_name)

    if existing_seat:
        room, row, seat = existing_seat
        return (
            f"DUPLICATE: {student_name} is already assigned "
            f"to {room}, Row {row + 1}, Seat {seat + 1}."
        )

    # Validate classroom name.
    if room_name not in classrooms:
        return "ERROR: Classroom does not exist."

    rows = classrooms[room_name]

    # Find the first vacant seat.
    for row_index, row in enumerate(rows):
        for seat_index, seat in enumerate(row):
            if seat is None:
                rows[row_index][seat_index] = student_name

                return (
                    f"SUCCESS: {student_name} allocated to "
                    f"{room_name}, Row {row_index + 1}, "
                    f"Seat {seat_index + 1}."
                )

    return f"NO VACANT SEATS: {room_name} is full."


def display_classrooms(classrooms):
    print("\n" + "=" * 60)
    print("              CLASSROOM SEATING PLAN")
    print("=" * 60)

    for room_name, rows in classrooms.items():
        print(f"\n{room_name}")
        print("-" * 40)

        for row_index, row in enumerate(rows):
            seats = []

            for seat_index, seat in enumerate(row):
                if seat is None:
                    seat_display = f"Seat {seat_index + 1}: VACANT"
                elif seat == "RESERVED":
                    seat_display = f"Seat {seat_index + 1}: RESERVED"
                else:
                    seat_display = f"Seat {seat_index + 1}: {seat}"

                seats.append(seat_display)

            print(f"Row {row_index + 1}: " + " | ".join(seats))


def calculate_capacity(classrooms):
    total_seats = 0
    occupied_seats = 0
    reserved_seats = 0
    vacant_seats = 0

    for rows in classrooms.values():
        for row in rows:
            for seat in row:
                total_seats += 1

                if seat is None:
                    vacant_seats += 1
                elif seat == "RESERVED":
                    reserved_seats += 1
                else:
                    occupied_seats += 1

    available_capacity = total_seats - reserved_seats

    print("\n" + "=" * 50)
    print("           OCCUPANCY SUMMARY")
    print("=" * 50)
    print(f"Total seating positions: {total_seats}")
    print(f"Occupied seats:         {occupied_seats}")
    print(f"Reserved seats:         {reserved_seats}")
    print(f"Vacant seats:           {vacant_seats}")
    print(f"Available capacity:     {available_capacity}")
    print(f"Remaining vacancies:    {vacant_seats}")

    if available_capacity > 0:
        occupancy_rate = (occupied_seats / available_capacity) * 100
    else:
        occupancy_rate = 0

    print(f"Occupancy rate:         {occupancy_rate:.2f}%")
    print("=" * 50)


def main():
    classrooms = create_classrooms()

    while True:
        print("\n===== CLASSROOM OCCUPANCY SYSTEM =====")
        print("1. Display classroom seating")
        print("2. Allocate a student")
        print("3. Calculate occupancy and vacant capacity")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            display_classrooms(classrooms)

        elif choice == "2":
            student_name = input("Enter student name: ")
            room_name = input(
                "Enter classroom (Room A, Room B, Room C): "
            ).strip()

            result = allocate_student(
                classrooms, student_name, room_name
            )
            print(result)

        elif choice == "3":
            calculate_capacity(classrooms)

        elif choice == "4":
            print("Exiting classroom occupancy system.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
