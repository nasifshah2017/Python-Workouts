re.compile(r'''
(\d\d\d-)      # area code
(\(\d\d\d\) )  # -or- area code with parens and no dash
\d\d\d      # fist 3 digits
-           # second dash
\d\d\d\d    # last 4 digits 
\sx\d{2,4}  # extension, like x1234''', re.IGNORECASE | re.DOTALL | re.VERBOSE)
