import json

class JsonStorage:

    # save family expenses to JOSN
    def save_expenses(self, Expenses):
        period = input("Family expense month (YYYY-MM):")
        family_records=[]

        for expense in Expenses:
            if expense["date"][:7]== period:
                family_records.append(expense)

            print(family_records)





    #open saved family expenses
    def load_expenses(self):
        pass