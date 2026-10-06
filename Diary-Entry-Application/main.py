from diary import add_entry, view_entries, filter_entries


def main():
    file_name = input("Enter the diary file name: ")
    while True:
            print("\nDiary Entry Application")
            print("1. Add diary entry")
            print("2. View all entries")
            print("3. Filter entries by date")
            print("4. Change diary file")
            print("5. Exit")

            choice = input("Choose an option: ")
            if choice == "1":
                date = input("Enter the date: ")
                entry = input("Enter your diary entry: ")
                add_entry(file_name, date, entry)
                print("Entry saved.")
            elif choice == "2":
                 view_entries(file_name)
            elif choice == "3":
                search_date = input("Enter the date to search: ")
                filter_entries(file_name, search_date)
            elif choice == "4":
                file_name = input("Enter the new diary file name: ")
            elif choice == "5":
                    print("Goodbye!")
                    break


if __name__ == "__main__":
    main()