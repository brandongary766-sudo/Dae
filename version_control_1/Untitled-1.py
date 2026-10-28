
print("Welcome to the Expense Tracker!")
input("Hello! Press Enter to continue. ")

expenses = []

def start_expense_tracker():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter expense amount: $"))
            category = input("Enter category: ")
            date = input("Enter date (MM/DD/YYYY): ")
            description = input("Enter description: ")

            expense = {
                "amount": amount,
                "category": category,
                "date": date,
                "description": description
            }

            expenses.append(expense)
            print("Expense saved successfully!")

        elif choice == "2":
            if len(expenses) == 0:
                print("No expenses recorded yet.")
            else:
                print("\n--- Your Expenses ---")
                for expense in expenses:
                    print("Amount: $", expense["amount"])
                    print("Category:", expense["category"])
                    print("Date:", expense["date"])
                    print("Description:", expense["description"])
                    print("--------------------")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

start_expense_tracker()
