
def calculate_average(marks):
    return sum(marks) / len(marks)


def assign_grade(average):
    if average >= 90:
        return "S"
    elif average >= 80:
        return "A"
    elif average >= 65:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def get_remark(average):
    if average >= 90:
        return "Outstanding Performance"
    elif average >= 80:
        return "Excellent Performance"
    elif average >= 65:
        return "Good Performance"
    elif average >= 50:
        return "Average Performance"
    else:
        return "Needs Improvement"


def display_student(name, department, semester, marks):
    average = calculate_average(marks)
    grade = assign_grade(average)

    print("\n===== STUDENT REPORT =====")
    print("Student Name:", name)
    print("Department:", department)
    print("Semester:", semester)

    for i, mark in enumerate(marks, start=1):
        print(f"Subject {i} Marks:", mark)
        if mark < 50:
            print(f"Warning: Subject {i} marks are below 50!")

    print("Total Marks:", sum(marks))
    print("Average Marks:", round(average, 2))
    print("Grade:", grade)
    print("Performance:", get_remark(average))


def main():
    print("===== STUDENT DETAILS AND GRADE CALCULATOR =====")

    name = input("Enter student name: ")
    department = input("Enter department: ")
    semester = input("Enter semester: ")

    marks = []

    for i in range(1, 4):
        mark = float(input(f"Enter marks for subject {i}: "))

        if mark < 0 or mark > 100:
            print("Invalid marks! Enter marks between 0 and 100.")
            return

        marks.append(mark)

    display_student(name, department, semester, marks)


if __name__ == "__main__":
    main()
