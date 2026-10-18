print("Student Grade Analyzer")
print()

scores = []

for i in range(5):
    score = float(input(f"Enter score for Student {i + 1}: "))
    scores.append(score)

print()

print("Student Scores:")
for score in scores:
    print(f"{score:g}")

print()

passed_count = 0
failed_count = 0

for i, score in enumerate(scores, start=1):

    if score >= 90:
        rating = "Excellent"
        status = "Passed"
        passed_count += 1
    elif score >= 80:
        rating = "Very Good"
        status = "Passed"
        passed_count += 1
    elif score >= 75:
        rating = "Good"
        status = "Passed"
        passed_count += 1
    else:
        rating = "Failed"
        status = "Failed"
        failed_count += 1

    print(f"Student {i}: {score:g} - {rating} - {status}")

print()

total_score = sum(scores)
average_score = total_score / len(scores)
highest_score = max(scores)

print(f"Total Score: {total_score:g}")
print(f"Average Score: {average_score:.1f}")
print(f"Highest Score: {highest_score:g}")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")