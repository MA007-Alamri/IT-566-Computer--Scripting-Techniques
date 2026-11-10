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
        print(os.path.abspath(filename))
        with open (filename, "w") as family_file:
         family_file.write(json.dumps(family_records, indent=4))


    #open saved family expenses
    def load_expenses(self):
        pass