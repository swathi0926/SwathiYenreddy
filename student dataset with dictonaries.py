students = {}
n = int(input("Enter number of students: "))
for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    marks = float(input(f"Enter marks of {name}: "))
    students[name] = marks
topper = max(students, key=students.get)
print("\n--- Students Data ---")
for name, marks in students.items():
    print(f"{name} : {marks}")
print(f"\nTopper is: {topper} with {students[topper]} marks")
