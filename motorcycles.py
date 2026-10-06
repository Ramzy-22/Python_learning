motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# Modifying Elements in a List
# motorcycles[0] = 'ducati'
# print(motorcycles)
# Adding Elements to a List
# Appending Elements to the End of a List
motorcycles.append('ducati')
print(motorcycles)
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
# Inserting Elements into a List
motorcycles.insert(0, 'ducati')
print(motorcycles)
# Removing Elements from a List
# Removing an Item Using the del Statement
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[1]
print(motorcycles)

# Removing an Item Using the pop() Method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

# Popping Items from any Position in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")

""" when you want to delete an item from a list
and not use that item in any way, use the del statement; if you want to use an
item as you remove it, use the pop() method"""

# Removing an Item by Value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

# The remove() method deletes only the first occurrence of the value you specify. If there’s
# a possibility the value appears more than once in the list, you’ll need to use a loop to
# determine if all occurrences of the value have been removed.

# Exercise 3-4 Guest List
guest_list = ['chiwanza', 'garven', 'judy']
print("Hello " + guest_list[0].title() + ", I am invinting you to my Birthday dinner.")
print("Hello " + guest_list[1].title() + ", I am invinting you to my Birthday dinner.")
print("Hello " + guest_list[2].title() + ", I am invinting you to my Birthday dinner.")

# Exercise 3-5 Changing Guest List
print("Hello " + guest_list[0].title() + ", I am invinting you to my Birthday dinner.")
print("Hello " + guest_list[1].title() + ", I am invinting you to my Birthday dinner.")
print("Hello " + guest_list[2].title() + ", I am invinting you to my Birthday dinner.")
print("Hello Micheal this is " + guest_list[-1] + ', I am sorry to inform you that can\'t make it.')
guest_list[-1] = 'simon'
print("\nHello " + guest_list[0].title() + ", I am invinting you to my Birthday dinner.")
print("Hello " + guest_list[1].title() + ", I am invinting you to my Birthday dinner.")
print("Hello " + guest_list[2].title() + ", I am invinting you to my Birthday dinner.")

# Exercise More Guests
print("\nHello guy I have found a bigger table so I am going to invite more people.")
guest_list.insert(0,'paul')
guest_list.insert(2,'bruce')
guest_list.append('elijah')
# Exercise 3-9. Dinner Guests
print("I am inviting " + str(len(guest_list)) + " people to my Birthday dinner.")
print("Hello " + guest_list[-6].title() + ", I am invinting you to my Birthday dinner.")
print("Hello " + guest_list[-5].title() + ", I am invinting you to my Birthday dinner.")
print("Hello " + guest_list[-4].title() + ", I am invinting you to my Birthday dinner.")
print("Hello " + guest_list[-3].title() + ", I am invinting you to my Birthday dinner.")
print("Hello " + guest_list[-2].title() + ", I am invinting you to my Birthday dinner.")
print("Hello " + guest_list[-1].title() + ", I am invinting you to my Birthday dinner.")

# 3-7. Shrinking Guest List
print("\nSorry guy but an unforseen problem has occured an I can only manage to invite two people.\n")
print("Hello "+ guest_list.pop().title() +".I am sorry to inform you that I can not invite you to my Birthday dinner.")
print("Hello "+ guest_list.pop().title() +".I am sorry to inform you that I can not invite you to my Birthday dinner.")
print("Hello "+ guest_list.pop().title() +".I am sorry to inform you that I can not invite you to my Birthday dinner.")
print("Hello "+ guest_list.pop().title() +".I am sorry to inform you that I can not invite you to my Birthday dinner.")
print(guest_list)
print("Hello " + guest_list[0].title() + ", I wanna let you know that you are still invited to my Birthday dinner.")
print("Hello " + guest_list[1].title() + ", I wanna let you know that you are still invited to my Birthday dinner.")
del guest_list[0]
del guest_list[0]
print(guest_list)