def add_entry(file, date, text):
    diary = open(file,"a")
    print(date, text, file=diary)
    diary.close()

def view_entries(file):
    diary = open (file)
    print(diary.read())
    diary.close()

def filter_entries(file, date):
    diary = open(file)
    for line in diary:
     if line.startswith(date + " "):
      print(line.strip())
    diary.close()