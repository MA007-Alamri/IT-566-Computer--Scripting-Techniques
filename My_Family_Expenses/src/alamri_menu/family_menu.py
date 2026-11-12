from alamri_spending.monthly_expenses import MonthlyExpenses

from alamri_storage.json_storage import JsonStorage

from alamri_reports.csv_report import FamilyCSVReport

class ExpenseFamilyMenu:
    def __init__(self):
        self.tracker = MonthlyExpenses()
        self.storage = JsonStorage()
        self.report = FamilyCSVReport()

    def display_menu(self):
        while True:
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

           if choice == "2":
              self.tracker.view_expenses()

           if choice =="3":
               self.tracker.find_expenses()

           if choice =="4":
               self.tracker.total_expenses()

           if choice =="5":
               self.storage.save_expenses(self.tracker.expenses)

           if choice=="6":
               self.storage.load_expenses()

           if choice=="7":
               self.report.export_expenses(self.tracker.expenses)
                 
           if choice == "8":
               print("Happy saving!")
               break
