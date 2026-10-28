def calculate_statistics(*grades, **options):
    if not grades:
        return None, None, 0, {}

    minimum = min(grades)
    maximum = max(grades)
    average = sum(grades) / len(grades)

    distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

    for grade in grades:
        if grade >= 90:
            distribution["A"] += 1
        elif grade >= 80:
            distribution["B"] += 1
        elif grade >= 70:
            distribution["C"] += 1
        elif grade >= 60:
            distribution["D"] += 1
        else:
            distribution["F"] += 1

    if options.get("show_distribution", True):
        return minimum, maximum, average, distribution

    return minimum, maximum, average, {}


minimum, maximum, average, distribution = calculate_statistics(
    85, 92, 76, 64, 90,
    show_distribution=True
)

print("Student Grades: 85, 92, 76, 64, 90")
print("Minimum Grade:", minimum)
print("Maximum Grade:", maximum)
print("Average Grade:", round(average, 2))
print("Letter Grade Distribution:", distribution)
