# Sorting a List Permanently with the sort() Method
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)
# Sorting in reverse
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort(reverse=True)
print(cars)

# Sorting a List Temporarily with the sorted() Function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the sorted list:")
print(cars)
# Sorting in reverse
print("\nHere is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars,reverse=True))

print("\nHere is the sorted list:")
print(cars,"\n")

# NOTE!!!
# Sorting a list alphabetically is a bit more complicated when all the values are not in
# lowercase. There are several ways to interpret capital letters when you’re deciding on
# a sort order, and specifying the exact order can be more complex than we want to deal
# with at this time. However, most approaches to sorting will build directly on what you
# learned in this section.

# Printing a List in Reverse Order
print(cars)

cars.reverse()
print(cars)
# The reverse() method changes the order of a list permanently, but you
# can revert to the original order anytime by applying reverse() to the same
# list a second time.

# Finding the Length of a List
print(len(cars))
# Python counts the items in a list starting with one, so you shouldn’t run into any off-
# by-one errors when determining the length of a list.

# Exercise 3-8 Seeing the world
locations = ['new york', 'london', 'tokyo', 'paris', 'moscow']
print(locations)
print(sorted(locations))
print(locations)
print(sorted(locations,reverse=True))
print(locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)

# 3-10. Every Function:
family = ['rudo', 'cholwe', 'chabota', 'micheal', 'michelo', 'renee']
print(family)

family.append('mary')
print(family)

family.insert(1, 'maambo')
print(family)

last_in_list = family.pop()
print(last_in_list)

last_born = family.pop(-1)
print(last_born)
family.append("renee")

del family[1]
print(family)

family.remove('rudo')
print(family)

print(sorted(family))
print(sorted(family,reverse=True))
print(family)
family.sort()
print(family)
family.sort(reverse=True)
print(family)
family = ['rudo', 'cholwe', 'chabota', 'micheal', 'michelo', 'renee']
print(family)
family.reverse()
print(family)
print("The current number of people in the Chikange family is " + str(len(family)) + ".")

# Exercise 3-11. Intentional Error:
print(family[-1])