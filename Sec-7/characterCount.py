message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}  # 'r': 12 


for character in message:
    # Its like saying no matter how many character, you start with 0
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)

#   {  'I': 1, 't': 6, ' ': 13, 'w': 2, 'a': 4, 's': 3, 'b': 1, 'r': 5, 'i': 6, 'g': 2,
#  'h': 3, 'c': 3, 'o': 2, 'l': 3, 'd': 3, 'y': 1, 'n': 4, 'A': 1, 'p': 1, ',': 1,
#  'e': 5, 'k': 2, '.': 1}


