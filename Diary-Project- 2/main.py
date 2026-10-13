from diary import add_entry, view_entries, filter_entries

file = input("choose a file: ")
while True:
    print("""1. Add entry
2. View entries
3. Search by date
4. Change diary file 
5. Exit""")



    choice = input("Your choice: ")
    if choice=="1":
        date = input("date:")
        text = input("Entry: ")
        add_entry(file, date, text)
    if choice== "2":
        view_entries(file)
    if choice== "3":
        date = input("Search date")
        filter_entries(file,date)
    if choice=="4":
        file= input("change diary file")
    if choice=="5":
        break

