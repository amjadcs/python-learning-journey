expenses = []
def add_expense():
name = input(“Enter expense name: “)
amount = float(input(“Enter expense amount: “))
category = input(“Enter expense category: “)
expense = {
    "name": name,
    "amount": amount,
    "category": category
}

expenses.append(expense)
print("Expense added successfully!")
def view_expenses():
if not expenses:
print(“No expenses recorded.”)
return
for expense in expenses:
    print(
        "Name:", expense["name"],
        "| Amount:", expense["amount"],
        "| Category:", expense["category"]
    )
def show_total():
total = sum(expense[“amount”] for expense in expenses)
print(“Total expenses:”, total)
while True:
print(”\nPersonal Expense Tracker”)
print(“1. Add Expense”)
print(“2. View Expenses”)
print(“3. Show Total”)
print(“4. Exit”)
choice = input("Choose an option: ")

if choice == "1":
    try:
        add_expense()
    except ValueError:
        print("Please enter a valid amount.")

elif choice == "2":
    view_expenses()

elif choice == "3":
    show_total()

elif choice == "4":
    print("Goodbye!")
    break

else:
    print("Invalid choice. Please try again.")
