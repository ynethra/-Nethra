import os
FILE_NAME = "students.txt"
def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    with open(FILE_NAME, "a") as f:
        f.write(f"{roll},{name},{marks}\n")

    print("Student added successfully!\n")
def view_students():
    if not os.path.exists(FILE_NAME):
        print("No records found!\n")
        return
    print("\n Student List:")
    print("Roll | Name | Marks")
    print("----------------------")

    with open(FILE_NAME, "r") as f:
        for line in f:
            roll, name, marks = line.strip().split(",")
            print(roll, "|", name, "|", marks)
    print()
def search_student():
    roll_search = input("Enter Roll Number to search: ")
    found = False
    with open(FILE_NAME, "r") as f:
        for line in f:
            roll, name, marks = line.strip().split(",")
            if roll == roll_search:
                print("\n Student Found!")
                print("Roll:", roll)
                print("Name:", name)
                print("Marks:", marks)
                found = True
                break
    if not found:
        print(" Student not found!\n")
def delete_student():
    roll_delete = input("Enter Roll Number to delete: ")

    found = False
    new_data = []

    with open(FILE_NAME, "r") as f:
        for line in f:
            roll, name, marks = line.strip().split(",")

            if roll != roll_delete:
                new_data.append(line)
            else:
                found = True

    with open(FILE_NAME, "w") as f:
        f.writelines(new_data)

    if found:
        print("Student deleted successfully!\n")
    else:
        print(" Student not found!\n")



while True:
    print("====== Student Management System ======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print(" Exiting... Goodbye!")
        break
    else:
        print("Invalid choice!\n")