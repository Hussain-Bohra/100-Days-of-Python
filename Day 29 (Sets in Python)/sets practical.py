# set declaring and inialization
# use {} curly brackets to create a set
myset = {"John", 20, True, 5.4, 20, "John"}
# here we store duplicate items but set will not allow to print duplicate items.
print(myset)

# because set are unordered collection, hence we cannot access it using index no.
# print(myset[0]) # throws an error
# print(myset[1]) # throws an error


# Quick Quiz Solution :-
# How to declare an empty set?
emptySet1 = {} # wrong, this will consider as dictionary in python.
print(type(emptySet1))

emptySet2 = set() # this is the correct way to declare an empty set in python.
print(type(emptySet2))


# Accessing set items using for loop :-
mynewset = {"John", "Brock", 20, True, False, 3.14}
for items in mynewset:
    print(items)


