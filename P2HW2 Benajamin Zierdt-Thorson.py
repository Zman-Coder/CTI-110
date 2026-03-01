#Benajamin Zierdt-Thorson
#01MAR2026
#P2HW2.py
#Grades Calculator

grade1 = float(input("Enter Grade for Module 1: "))
grade2 = float(input("Enter Grade for Module 2: "))
grade3 = float(input("Enter Grade for Module 3: "))
grade4 = float(input("Enter Grade for Module 4: "))
grade5 = float(input("Enter Grade for Module 5: "))
grade6 = float(input("Enter Grade for Module 6: "))

grades = []

grades.append(grade1)
grades.append(grade2)
grades.append(grade3)
grades.append(grade4)
grades.append(grade5)
grades.append(grade6)

print("------------Results------------")
lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total / len(grades)
print(f"{'Lowest Grade:':<20}{lowest:.1f}")
print(f"{'Highest Grade:':<20}{highest:.1f}")
print(f"{'Sum of Grades:':<20}{total:.1f}")
print(f"{'Average:':<20}{average:.2f}")
print("-" * 39)