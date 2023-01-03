# 1. isdisjoint() :-
# The isdisjoint() method checks if items of given set are present in another set. This method returns False if items are present, else it returns True.

# Example :-
# cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Nairobi", "Seoul", "Kabul", "Chicago"}

# print(cities1.isdisjoint(cities2)) # return true because cities2 items are not present in cities1.



# 2. issuperset() :-
# The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.

# Example :-
# cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Seoul", "Kabul", "Berlin"}
# print(cities1.issuperset(cities2))  # return false because only one item of cities2 are present in cities1.

# cities3 = {"Tokyo", "Delhi"}
# print(cities1.issuperset(cities3))  # return true because cities3 all items are present in cities1.




# 3. issubset()
# The issubset() method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False.

# Example :-
# cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Delhi", "Madrid"}
# print(cities2.issubset(cities1)) # return true because cities2 all items are present in cities1.



# 4. add()
# If you want to add a single item to the set use the add() method.

# Example :-
# cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities1.add("Helsinki")
# print(cities1) 




# 5. update()
# If you want to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary), and use the update() method to add it into the existing set.

# Example :-
# cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Helsinki", "Warsaw", "Seoul"}
# cities1.update(cities2)
# print(cities1)



# 6. remove()/discard()
# We can use remove() and discard() methods to remove items form list.
# The main difference between remove and discard is that, if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error.


# Example :-
# cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities1.remove("Tokyo")
# print(cities1)


# 7. pop()
# This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable.

# Example :-
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# item = cities.pop()
# print(cities)
# print(item)



# 8. del
# del is not a method, rather it is a keyword which deletes the set entirely.

# Example :-
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# del cities
# print(cities)



# 9. clear():
# This method clears all items in the set and prints an empty set.

# Example :-
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.clear()
# print(cities)



# 10. You can also check if an item exists in the set or not.
# Example :-
info = {"Brock", 19, False, 5.9}
if "Brock" in info:
    print("Brock is present.")
else:
    print("Brock is absent.")