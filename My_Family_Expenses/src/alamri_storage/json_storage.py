import json
import os

class JsonStorage:

    # save family expenses to JOSN
    def save_expenses(self, Expenses):
        period = input("Family expense month (YYYY-MM):")
        family_records=[]

        for expense in Expenses:
            if expense["date"][:7]== period:
                family_records.append(expense)

        filename = f"Alamri_Family_{period}.json"

        try:
            with open(filename,"r") as family_file:
                old_recordes = json.load(family_file)
        except FileNotFoundError:
            old_recordes=[]

        for expense in family_records:
            found= any(item==expense for item in old_recordes)
            if not found: old_recordes.append(expense)
        
        print(os.path.abspath(filename))
        with open (filename, "w") as family_file:
         family_file.write(json.dumps(old_recordes, indent=4))


    #open saved family expenses
    def load_expenses(self):
        pass