helloFile = open('/Users/nasifshah/Documents/Udemy/Python\ Programming/Sec-11/hello.txt ')
content = helloFile.read()
print(content)
helloFile.close()

helloFile = open('/Users/nasifshah/Documents/Udemy/Python\ Programming/Sec-11/hello.txt ')
helloFile.readlines()

# ['Hello world!\n', 'How are you?']
helloFile.close()

# Opening a file in a write mode
helloFile = open('/Users/nasifshah/Documents/Udemy/Python\ Programming/Sec-11/hello.txt ', 'w')

# Opening a file in an append mode
helloFile = open('/Users/nasifshah/Documents/Udemy/Python\ Programming/Sec-11/hello.txt ', 'a')

# Opening a new file by the name hello2.txt
helloFile = open('/Users/nasifshah/Documents/Udemy/Python\ Programming/Sec-11/hello2.txt ', 'w')

# In order to write on this file we need to use the write() method
helloFile.write('Hello!!!!!!!')

# Closing the file
helloFile.close()

