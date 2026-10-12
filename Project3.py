students = []

while True:
    print("\nWelcome to the Student Data Organizer!")
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nEnter student details:")

        student_id = input("Student ID: ")
        name = input("Name: ")
        age = input("Age: ")
        grade = input("Grade: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")
        subjects = input("Subjects (comma-separated): ")

        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "grade": grade,
            "dob": dob,
            "subjects": subjects
        }

        students.append(student)
        print("Student added successfully!")

    elif choice == "2":
        print("\n--- Display All Students ---")

        if len(students) == 0:
            print("No students found.")
        else:
            for student in students:
                print(
                    "Student ID:", student["id"],
                    "| Name:", student["name"],
                    "| Age:", student["age"],
                    "| Grade:", student["grade"],
                    "| Subjects:", student["subjects"]
                )

    elif choice == "3":
        student_id = input("Enter Student ID to update: ")

        for student in students:
            if student["id"] == student_id:
                student["name"] = input("Enter new name: ")
                student["age"] = input("Enter new age: ")
                student["grade"] = input("Enter new grade: ")
                student["dob"] = input("Enter new date of birth: ")
                student["subjects"] = input("Enter new subjects: ")

                print("Student information updated successfully!")
                break
        else:
            print("Student not found.")

    elif choice == "4":
        student_id = input("Enter Student ID to delete: ")

        for student in students:
            if student["id"] == student_id:
                students.remove(student)
                print("Student deleted successfully!")
                break
        else:
            print("Student not found.")

    elif choice == "5":
        print("\n--- Subjects Offered ---")
        subjects = ["Math", "Science", "English"]

        for subject in subjects:
            print(subject)

    elif choice == "6":
        print("\nThank you for using the Student Data Organizer!")
        break

    else:
        print("Invalid choice. Please try again.")
