import csv

class FamilyCSVReport:


    # Export family expenses to CSV
    def export_expenses(self, expenses):
        if not expenses:
            print(" No expenses to export.")
            return

        csv_name = "Alamri_Family_Report.csv"

        with open(csv_name,"w",newline="") as f:
            writer = csv.DictWriter(f, fieldnames=expenses[0].keys())
            writer.writeheader()
            writer.writerows(expenses)