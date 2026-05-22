module_name = input("Enter module name: ")
num_students = int(input("Enter number of students: "))

students = []
total = 0

for i in range(num_students):
    student_number = input("Enter student number: ")

    while True:
        mark = float(input("Enter final mark (0-100): "))
        if 0 <= mark <= 100:
            break
        else:
            print("Invalid mark. Please enter between 0 and 100.")

    students.append((student_number, mark))
    total += mark

average = total / num_students

top_student = max(students, key=lambda x: x[1])
lowest_student = min(students, key=lambda x: x[1])

print("\n--- ACADEMIC PERFORMANCE REPORT ---")
print("Module:", module_name)
print("Number of Students:", num_students)

print("\nStudent Results:")
for s in students:
    print(s[0], "-", s[1])

print("\nClass Average:", round(average, 2), "%")
print("Top Student:", top_student[0], "-", top_student[1], "%")
print("Lowest Student:", lowest_student[0], "-", lowest_student[1], "%")

