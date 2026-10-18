raw_records = [
    "Ana,88,92,90",
    "Ben,70,72,74",
    "Cara,95,91,94",
    "Dan,78,80,76",
    "Ella,85,89,87",
    # Test invalid records (Part F)
    "Fred,90,85",
    "Gina",
    "Henry,90,eighty,85",
    "Ivy,"
]

PASSING_GRADE = 75

student_scores = {}

# PART A & F: Read and check the records
for record in raw_records:
    fields = record.split(",")

    if len(fields) != 4:
        print(f"Skipped invalid record: {record}")
        continue

    name = fields[0]

    try:
        scores = [int(score) for score in fields[1:]]
    except ValueError:
        print(f"Skipped invalid record: {record}")
        continue

    student_scores[name] = scores


# PART B: Display the records
print("\nORGANIZED STUDENT RECORDS")

for name in sorted(student_scores):
    print(name, student_scores[name])


# PART C: Calculate student grades
results = []

passed = 0
failed = 0

for name in student_scores:
    scores = student_scores[name]

    total = sum(scores)
    average = total / len(scores)
    highest = max(scores)
    lowest = min(scores)

    if average >= PASSING_GRADE:
        remark = "Passed"
        passed += 1
    else:
        remark = "Failed"
        failed += 1

    results.append([name, average, highest, lowest, remark])


# PART D: Arrange ranking
results.sort(key=lambda x: x[1], reverse=True)

print("\nSTUDENT GRADE REPORT")
print("Rank  Name    Average  Highest  Lowest  Remark")

rank = 1

for student in results:
    print(
        f"{rank:<6}{student[0]:<8}"
        f"{student[1]:<9.2f}"
        f"{student[2]:<9}"
        f"{student[3]:<8}"
        f"{student[4]}"
    )
    rank += 1


# PART E: Class summary
total_students = len(results)

class_average = 0

for student in results:
    class_average += student[1]

if total_students > 0:
    class_average = class_average / total_students

print("\nCLASS SUMMARY")
print("Number of Students:", total_students)
print("Passed:", passed)
print("Failed:", failed)
print(f"Class Average: {class_average:.2f}")

if total_students > 0:
    print(f"Highest: {results[0][0]} - {results[0][1]:.2f}")
    print(f"Lowest: {results[-1][0]} - {results[-1][1]:.2f}")