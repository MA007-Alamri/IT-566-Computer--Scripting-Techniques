import json
import os

class JsonStorage:

    # save family expenses to JOSN

    def save_expenses(self, Expenses):
        period = input("Family expense month (YYYY-MM):")
        family_records = self.filter_month_expenses(Expenses, period)

        filename = f"Alamri_Family_{period}.json"

        try:
            old_recordes = self.read_json_file(filename)  
        except FileNotFoundError:
            old_recordes=[]

        old_recordes = self.merge_expenses(old_recordes, family_records)
        
        print(os.path.abspath(filename))
        self.write_json_file(filename, old_recordes)

    def write_json_file(self, filename, records):
        with open(filename, "w") as family_file:
           family_file.write(json.dumps(records, indent=4))

    def filter_month_expenses(self, Expenses, period):
        family_records = []

        for expense in Expenses:
            if expense["date"][:7] == period:
                family_records.append(expense)

        return family_records

    def merge_expenses(self, old_records, family_records):
        for expense in family_records:
            found = any(item == expense for item in old_records)
            if not found:
                old_records.append(expense)

        return old_records

    #open saved family expenses

    def display_load_menu(self):
        print("Open Saved Family Expenses")
        print("1. Open by Category")
        print("2. Open by Date")
        print("3. Back to Main Menu")

    def read_json_file(self, filename):
        with open(filename, "r") as family_file:
            return json.load(family_file)
        
    def load_expenses(self):
        self.display_load_menu()

        load_choice = input("Choose an option: ")

        if load_choice == "1":
            family_category = input("Choose a category: ")
            family_month = input("Choose a month (YYYY-MM): ")

        elif load_choice == "2":
            family_date = input("Choose a date (YYYY-MM-DD): ")
            family_month = family_date[:7]

        else:
            return

        filename = f"Alamri_Family_{family_month}.json"


        try:
            saved_expenses = self.read_json_file(filename)

        except FileNotFoundError:
            print("No saved expenses found for this month.")
            return

        except json.JSONDecodeError:
            print("The JSON file is not valid.")
            return

        print("\nAlamri Family Expenses")

        self.display_saved_expenses(saved_expenses, load_choice, family_category if load_choice == "1" else None, family_date if load_choice == "2" else None)             

    def display_saved_expenses(self, saved_expenses, load_choice, family_category=None, family_date=None):
        found= False
        
        for expense in saved_expenses:
            if load_choice == "1":
                if expense["category"].lower() == family_category.lower():
                   print(expense["category"], "-", expense["amount"], "-", expense["date"])
                   found= True
                
            elif load_choice == "2":
                if expense["date"] == family_date:
                   print(expense["category"], "-", expense["amount"], "-", expense["date"])
                   found= True
                
        if not found:
            print("No matching expenses found.")
                            
                            
