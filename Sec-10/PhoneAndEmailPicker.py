#! python3

import re, pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345

(
((\d\d\d)|(\(\d\d\d\)))?    # area code (optional)
(\s|-)    # first seperator
\d\d\d    # first 3 digits
-    # separator
\d\d\d\d    # last 4 digits
(((ext(\.)?\s)|x)   # extension word-part (optional)
(\d{2,5}))?         # extension number-part (optional)
)
''', re.VERBOSE)

# without the VERBOSE mode, the above code would've looked like this
# re.compile('((\d\d\d)|(\(\d\d\d\)))?(\s|-)\d\d\d-\d\d\d\d(((ext(\.)?\s)|x)(\d{2,5}))?')

# Create a regex for email addresses
emailRegex = re.compile(r'''
# some.+_thing@(\d{2,5}))?.com

[a-zA-Z0-9_.+]+    # name part
Blockchain         # @ symbol
[a-zA-Z0-9_.+]+    # domain name part

''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()


# Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# Copy the extracted email/phone to the clioboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
