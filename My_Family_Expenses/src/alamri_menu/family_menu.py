from alamri_spending.monthly_expenses import MonthlyExpenses

class ExpenseFamilyMenu:
    def __init__(self):
        self.tracker = MonthlyExpenses()

    def display_menu(self):
        print("Alamri Monthly Expense Tracker")
        print("1. Add Family Expense")
        print("2. View Monthly Expense")
        print("3. find Expenses")
        print("4. Total Expenses")
        print("5. Save Expenses to JSON")
        print("6. open JSON File")
        print("7. Download CSV Report")
        print("8. Exit")
        choice = input("Select a number from 1 to 8:")

        if choice == "1":
           amount = input("expense amount:$") 
           category = input("expense category:")
           date= input("expense date (YYYY-MM-DD):")
           expense = {"amount": float(amount),"category": category, "date": date}
           self.tracker.add_expense(expense)

