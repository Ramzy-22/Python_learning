bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
# accessing the first element
print(bicycles[0].title())
# returning the second and fourth bicycle
print(bicycles[1])
print(bicycles[3])
# a negative index reverse the way we access elements(-1 represents the last element)
#(-2 represents the secod last index)
print(bicycles[-1])
# Using individual values from a list
message = 'My first bicycle was a ' + bicycles[0].title() + '.'
print(message)
# Exercise 3-1 Names
friends = ['elijah', 'simon', 'paul', 'bruce', 'judy', 'chiwanza']
print(friends[-1])
print(friends[-2])
print(friends[-3])
print(friends[-4])
print(friends[-5])
print(friends[-6])

# Exercise 3-2 Greetings
message = "Hello, " + friends[0].title() + ". How are you?"
print(message)
message = "Hello, " + friends[1].title() + ". How are you?"
print(message)
message = "Hello, " + friends[2].title() + ". How are you?"
print(message)
message = "Hello, " + friends[3].title() + ". How are you?"
print(message)
message = "Hello, " + friends[4].title() + ". How are you?"
print(message)
message = "Hello, " + friends[5].title() + ". How are you?"
print(message)

# Exercise 3-3 Your own list
cars = ['BMW', 'mercedes', 'volxwagen', 'chevrolet']
message = "I would like to by a " + cars[0] + " when I become successful."
print(message)