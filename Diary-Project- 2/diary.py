def add_entry(file, date, text):
    with open(file,"a") as diary:
     diary.write(f'{date} {text}\n')

def view_entries(file):
    with open(file,'r') as diary:
       print(diary.read())

def filter_entries(file, date):
    with open(file, 'r') as diary:
        lines = diary.readlines()
        for line in lines:
           if line[:10] == date:
              print(line)
