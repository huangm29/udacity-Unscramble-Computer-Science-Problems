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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def is_fixed_Bangalore(number):
  return number[:5] == '(080)'

def is_fixed(number):
  return number[:2] == '(0'

def is_mobile(number):
  return number[0] == '7' or number[0] == '8' or number[0] == '9' and ' ' in number

def is_tele(number):
  return number[:3] == '140'

set_of_codes = set()
calls_from_fixed_Bangal = 0
calls_counted = 0
for call in calls:
  if is_fixed_Bangalore(call[0]): #From Bangalor
    calls_from_fixed_Bangal += 1
    if is_fixed(call[1]):
      last_index = call[1].find(')')
      set_of_codes.add(call[1][1:last_index])
    if is_mobile(call[1]):
      set_of_codes.add(call[1][:4])
    if is_tele(call[1]):
      set_of_codes.add('140')
    if is_fixed_Bangalore(call[1]):
      calls_counted +=1
    
set_of_codes = sorted(set_of_codes)
print("The numbers called by people in Bangalore have codes:")
for code in set_of_codes:
  print(code)
percentage = round(calls_counted/calls_from_fixed_Bangal*100,2)
print(F"{percentage} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore")
