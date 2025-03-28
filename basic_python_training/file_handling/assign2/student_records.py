import csv
import os

FILE_NAME = "/Users/consultadd/Desktop/python_training/file_handling/assign2/students.csv"
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "Grade"])

def add_student():
    name = input("Enter student name: ")
    age = input("Enter age: ")
    grade = input("Enter grade: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, age, grade])

    print(f"{name} added successfully!")

def delete_student():
    name_to_delete = input("Enter name to delete: ")
    students = []

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        header = next(reader) 
        for row in reader:
            if row[0].lower() != name_to_delete.lower():
                students.append(row)

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(students)

    print(f"{name_to_delete} deleted (if found)")

def search_student():
    """Searches for a student by name"""
    name_to_search = input("Enter name to search: ")

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader) 
        for row in reader:
            if row[0].lower() == name_to_search.lower():
                print(f"🔍 Found: Name: {row[0]}, Age: {row[1]}, Grade: {row[2]}")
                return

    print("Student not found!")

def display_students():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        data = list(reader)

    if len(data) <= 1:
        print("📂 No student records found.")
        return

    print("\n📜 Student Records:")
    for row in data:
        print("\t".join(row))

# Main:-
while True:
    print("\n📚 Student Records System")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Search Student")
    print("4. Display All Students")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        delete_student()
    elif choice == "3":
        search_student()
    elif choice == "4":
        display_students()
    elif choice == "5":
        print("Exiting... Have a great day!")
        break
    else:
        print("Invalid choice! Please try again.")
