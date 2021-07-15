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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
outgoing_num = set()
incoming_num = set()
text_num = {text[i] for i in range(2) for text in texts}
for call in calls:
    outgoing_num.add(call[0])
    incoming_num.add(call[1])
excluded_nums = text_num | incoming_num
telemakers = {num for num in outgoing_num if num not in excluded_nums}
telemakers = sorted(telemakers)
print("These numbers could be telemarketers: ")
for num in telemakers:
    print(num)

