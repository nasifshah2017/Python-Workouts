def div42by(divideBy):
    return 42 / divideBy

#   print(div42by(2))   # 21.0
#   print(div42by(12))  # 3.5
#   print(div42by(0))   # Error
#   print(div42by(1))   # Error


# Modifying the Function

def moddiv42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: You tried to divide by zero')


print(moddiv42by(2))   # 21.0
print(moddiv42by(12))  # 3.5
print(moddiv42by(0))   # Error: You tried to divide by zero
print(moddiv42by(1))   # 42.0


print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('Thats a lot of cats.')
    else:
        print('Thats not that many cats.')
except ValueError: 
    print('You did not enter a number.')

# Instead of throwing an error due to entering non-numeric value, the program
# will continue "You did not enter a number"
