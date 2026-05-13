import os
FILE_NAME = "expenses.txt"
def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category (food/travel/others): ")
    with open(FILE_NAME, "a") as f:
        f.write(f"{amount},{category}\n")
    print(" Expense added!\n")
def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses found!\n")
        return
    print("\n Expense List:")
    print("Amount | Category")
    print("-------------------")
    with open(FILE_NAME, "r") as f:
        for line in f:
            amount, category = line.strip().split(",")
            print(amount, "|", category)
    print()
def total_expense():
    if not os.path.exists(FILE_NAME):
        print("No expenses found!\n")
        return
    total = 0
    with open(FILE_NAME, "r") as f:
        for line in f:
            amount, _ = line.strip().split(",")
            total += float(amount)
    print(f"\nTotal Spending: {total}\n")
while True:
    print("======  Expense Tracker ======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("❌ Invalid choice!\n")