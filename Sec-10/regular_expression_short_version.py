import re

message = 'Call me at 415-555-1011 tomorrow, or at 415-555-9999 for my office line'

# 'd' stands for digits, here so we are looking for a number as ddd-ddd-dddd

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchObject = phone.NumRegex.search(message)
print(matchObject.group())  #   415-555-1011
