"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""
call_time = {}
for call in calls:
    time = int(call[3])
    call_time[call[0]] = call_time.get(call[0], 0) + time
    call_time[call[1]] = call_time.get(call[1], 0) + time
phone_num_most = max(call_time, key=call_time.get)
print(
    F"{phone_num_most} spent the longest time, {call_time[phone_num_most]} seconds, on the phone during September 2016.")
