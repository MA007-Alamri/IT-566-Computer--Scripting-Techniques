# Keep track of monthly family expenses

class MonthlyExpenses:
    def __init__(self):
        self.expenses = []


    #function to add a new family expense

    def add_expense(self, expense):
        self.expenses.append(expense)
        print("Expense added successfully.")

    #function to view all family expense

    def view_expenses(self):
        if not self.expenses:
            print ("No family expenses found.")
            return
        for expense in self.expenses:
            print (expense["date"], "-", expense["category"], "-", expense["amount"])


    #function to find expenses by date or category

    def find_expenses(self):
        pass

    #function to show total amount spent

    def total_expenses(self):
        pass




    
