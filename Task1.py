"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
phone_number = {text[i] for i in range(2) for text in texts} | {
    call[i] for i in range(2) for call in calls}
print(
    F"There are {len(phone_number)} different telephone numbers in the records.")
