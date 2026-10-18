#Part B – Classify a Grade

def classify_grade(grade):
    """Return the classification and status of a grade."""
    if grade >= 90:
        return "Excellent", "Passed"
    elif grade >= 85:
        return "Very Good", "Passed"
    elif grade >= 80:
        return "Good", "Passed"
    elif grade >= 75:
        return "Satisfactory", "Passed"
    else:
        return "Needs Improvement", "Failed"

# PART A – Load and Validate the Records

def load_students(filename):
    """Read valid student records from a text file and return them as a list."""
    students = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                # Remove surrounding whitespace
                cleaned_line = line.strip()
                # Skip blank lines
                if not cleaned_line:
                    continue

                parts = cleaned_line.split(",")
                if len(parts) != 3:
                    continue

                student_id = parts[0].strip()
                name = parts[1].strip()
                grade_str = parts[2].strip()

                try:
                    grade = float(grade_str)
                except ValueError:
                    continue
             
                if 0 <= grade <= 100:
             
                    students.append({
                        "student_id": student_id,
                        "name": name,
                        "grade": grade
                    })
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except OSError as e:
        print(f"Error accessing file '{filename}': {e}")

    return students


# PART C – Analyze the Class (Without using sum(), max(), or min())

def calculate_statistics(students):
    """Calculate and return the class statistics using loop and accumulators."""
    if not students:
        return None

    total_grade = 0
    passed_count = 0
    failed_count = 0
    highest_student = students[0]
    lowest_student = students[0]

    for student in students:
        grade = student["grade"]
        total_grade += grade

        _, status = classify_grade(grade)
        if status == "Passed":
            passed_count += 1
        else:
            failed_count += 1
            
        if grade > highest_student["grade"]:
            highest_student = student

        if grade < lowest_student["grade"]:
            lowest_student = student

    total_students = len(students)
    average_grade = total_grade / total_students if total_students > 0 else 0.0

    return {
        "total_students": total_students,
        "average": average_grade,
        "passed_count": passed_count,
        "failed_count": failed_count,
        "highest_student": highest_student,
        "lowest_student": lowest_student
    }


# PART D – Display All Students and Statistics

def display_students(students):
    """Display all student records in a formatted table."""
    if not students:
        print("No student records to display.")
        return

    print("\n" + "=" * 65)
    print(f"{'ID':<10} {'Name':<20} {'Grade':<8} {'Classification':<18} {'Status':<8}")
    print("=" * 65)

    for student in students:
        classification, status = classify_grade(student["grade"])
        name_display = student["name"][:18]
        print(f"{student['student_id']:<10} {name_display:<20} {student['grade']:<8.2f} {classification:<18} {status:<8}")
    print("=" * 65)


def display_statistics(statistics):
    """Display the calculated class statistics clearly."""
    if not statistics:
        print("No statistics available.")
        return

    print("\nCLASS STATISTICS")
    print("-" * 30)
    print(f"Number of students: {statistics['total_students']}")
    print(f"Class average:     {statistics['average']:.2f}")
    print(f"Passed:            {statistics['passed_count']}")
    print(f"Failed:            {statistics['failed_count']}")

    highest = statistics['highest_student']
    lowest = statistics['lowest_student']
    print(f"Highest:           {highest['name']} - {highest['grade']:.2f}")
    print(f"Lowest:            {lowest['name']} - {lowest['grade']:.2f}")
    print("-" * 30)


# PART E – Search for a Student

def search_student(students, keyword):
    """Return records matching keyword using lower() and partial matching."""
    matches = []
    clean_keyword = keyword.strip().lower()

    if not clean_keyword:
        return matches

    for student in students:
        student_id = student["student_id"].lower()
        name = student["name"].lower()

        if clean_keyword in student_id or clean_keyword in name:
            matches.append(student)

    return matches


# PART F – Save the Report

def save_report(students, statistics, filename="grade_report.txt"):
    """Write student records and class statistics to a text report file."""
    if not students or not statistics:
        print("Cannot save report: missing student data or statistics.")
        return

    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("=========================================================\n")
            file.write("                STUDENT GRADE ANALYZER REPORT           \n")
            file.write("=========================================================\n\n")

            file.write("STUDENT RECORDS:\n")
            file.write("-" * 57 + "\n")
            file.write(f"{'ID':<10} {'Name':<20} {'Grade':<8} {'Classification':<18} {'Status':<8}\n")
            file.write("-" * 57 + "\n")

            for student in students:
                classification, status = classify_grade(student["grade"])
                file.write(f"{student['student_id']:<10} {student['name']:<20} {student['grade']:<8.2f} {classification:<18} {status:<8}\n")

            file.write("\n" + "=" * 57 + "\n")
            file.write("CLASS STATISTICS:\n")
            file.write("-" * 57 + "\n")
            file.write(f"Number of students: {statistics['total_students']}\n")
            file.write(f"Class average:     {statistics['average']:.2f}\n")
            file.write(f"Passed:            {statistics['passed_count']}\n")
            file.write(f"Failed:            {statistics['failed_count']}\n")

            highest = statistics['highest_student']
            lowest = statistics['lowest_student']
            file.write(f"Highest:           {highest['name']} - {highest['grade']:.2f}\n")
            file.write(f"Lowest:            {lowest['name']} - {lowest['grade']:.2f}\n")
            file.write("=========================================================\n")

        print(f"\nReport successfully saved to '{filename}'.")
    except OSError as e:
        print(f"Error writing report to file '{filename}': {e}")


# PART G – Complete the Menu Loop

def main():
    """Run the menu-driven Student Grade Analyzer."""
    students = load_students("grades.txt")

    if not students:
        print("No valid student records were loaded.")
        return

    statistics = calculate_statistics(students)

    while True:
        print("\nSTUDENT GRADE ANALYZER")
        print("[1] Display all students")
        print("[2] Display class statistics")
        print("[3] Search for a student")
        print("[4] Save report")
        print("[5] Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_students(students)
        elif choice == "2":
            display_statistics(statistics)
        elif choice == "3":
            keyword = input("Enter student name or ID to search: ")
            results = search_student(students, keyword)
            if results:
                print(f"\nFound {len(results)} matching record(s):")
                display_students(results)
            else:
                print("\nNo matching student found.")
        elif choice == "4":
            save_report(students, statistics, "grade_report.txt")
        elif choice == "5":
            print("\nExiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
            continue


if __name__ == "__main__":
    main()