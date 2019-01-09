message = 'Hello World'

print(message.lower())
print(message.upper())
print(len(message))
print(message.find('Universe'))

greeting = 'Hello'
name = 'Krishna'
message = greeting + ', ' + name
print(message)

message = '{}, {}'.format(greeting, name)
print(message)

# fstrings are supported in 3.6 or higher
message = f'{greeting}, {name}'
print(message)

# prints all attributes and methods for that variable
print(dir(message)) # pass object

print(help(str))    # pass class
