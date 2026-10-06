def add_entry(file_name, date, entry):
    with open(file_name, "a") as diary_file:
        diary_file.write(f"{date}|{entry}\n")


def view_entries(file_name):
    with open(file_name, "r") as diary_file:
        for line in diary_file:
            print(line.strip())


def filter_entries(file_name, search_date):
    with open(file_name, "r") as diary_file:
        for line in diary_file:
            if line.startswith(search_date + "|"):
                print(line.strip())