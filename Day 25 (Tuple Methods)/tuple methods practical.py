# We know tuples are immutable, we cannot change it directly.
# Hence we can change it by converting tuple to a list and then list to a tuple.

oldtuple = ("Red", "Green", "Yellow")
print("old tuple:",oldtuple)
# converting tuple to a list
mylist = list(oldtuple)
# adding one more element
mylist.append("Cyan")
# print(mylist)

# now converting list to a tuple
oldtuple = tuple(mylist)
print("new tuple:",oldtuple)



# --> tuple methods

# 1. len() method
# The len() method returns the length of the tuple.
# Example :-
tup1 = ("Red", "Green", "Blue", "Yellow")
print("Length of tup1 is:",len(tup1))



# 2. count() method
# The count() method of Tuple returns the number of times the given element appears in the tuple.
# Example :-
tup2 = (1, 3, 5, 7, 9, 3, 10)
print("How many 3's are there:",tup2.count(3))



# 3. index() method
# The index() method returns the first occurrence of the given element from the tuple.
# Example :-
tup3 = (1, 3, 5, 7, 5, 3, 10, 5)
print("First Occurence of 5 is:",tup3.index(5))

