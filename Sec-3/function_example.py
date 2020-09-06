# Functions

def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.!')


#   hello()
#   hello()
#   hello()

def plusOne(number):
    return number + 1

newNumber = plusOne(5)
#   print(newNumber)

spam = 42       # global variable

def eggs():
    spam = 42   # local variable


print('Some code here.')
print('Some more code.')
