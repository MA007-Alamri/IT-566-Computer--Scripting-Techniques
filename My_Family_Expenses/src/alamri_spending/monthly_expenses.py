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
        print("Find Family Expenses")
        print("1. search by category")
        print("2. search by date")
        print("3. search by category and date")
        print("4. back to main menu")
        search_choice = input("choose a search option(1-4):")

        if search_choice =="1":
            category =input("search for a category:")
            for item in self.expenses:
                if item["category"]== category:
                    print(item["date"], "$", item["amount"])




    #function to show total amount spent

    def total_expenses(self):
        pass




    
