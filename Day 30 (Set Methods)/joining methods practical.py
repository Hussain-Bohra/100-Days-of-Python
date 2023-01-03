# Set Methods :-
# 1. union() and update() :-
# The union() and update() methods prints all items that are present in the two sets. The union() method returns a new set whereas update() method adds item into the existing set from another set.

# Example 1 - using union() :-
# set1 = {"Tokyo", "Berlin", "Nairobi", "Rio", "Denver"}
# set2 = {"New York", "Tokyo", "Chicago", "Berlin"}
# print(f"Add set1 & set2 values in set1: {set1.union(set2)}")

# After using union() :-
# print("After using union() :-")
# print(f"set1: {set1}") # by using union(), set1 is not updated


# Example 2 - using update() :-
# set1 = {"Tokyo", "Berlin", "Nairobi", "Rio", "Denver"}
# set2 = {"New York", "Tokyo", "Chicago", "Berlin"}
# set1.update(set2)

# After using update() :-
# print("After using update() :-")
# print(f"set1: {set1}") # by using update(), set1 is also updated

 


# 2. intersection and intersection_update() :-
# The intersection() and intersection_update() methods prints only items that are similar to both the sets. The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set.

# Example 1 - using intersection() :-
# set1 = {"Tokyo", "Berlin", "Nairobi", "Rio", "Denver"}
# set2 = {"New York", "Tokyo", "Chicago", "Berlin"}
# print(f"Common Values in Both Sets are: {set1.intersection(set2)}")

# After using intersection() :-
# print("After using intersection() :-")
# print(f"set1: {set1}") # by using intersection(), set1 is not updated


# Example 2 - using intersection_update() :-
# set1 = {"Tokyo", "Berlin", "Nairobi", "Rio", "Denver"}
# set2 = {"New York", "Tokyo", "Chicago", "Berlin"}
# set1.intersection_update(set2)

# After using intersection_update() :-
# print("After using intersection_update() :-")
# print(f"set1: {set1}") # by using intersection_update(), set1 is also updated




# 3. symmetric_difference and symmetric_difference_update() :-
# The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets. The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set.

# Example 1 - using symmetric_difference :-
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# print(f"Unique Values from Both Sets are: {cities.symmetric_difference(cities2)}")

# After using symmetric_difference() :-
# print("After using symmetric_difference() :-")
# print(f"cities: {cities}") # by using symmetric_difference(), cities is not updated


# Example 2 - using symmetric_difference_update() :-
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities.symmetric_difference_update(cities2)
# print(cities)

# After using symmetric_difference_update() :-
# print("After using symmetric_difference_update() :-")
# print(f"cities: {cities}") # by using symmetric_difference_update(), cities is also updated




# 4. difference() and difference_update() :-
# The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets. The difference() method returns a new set whereas difference_update() method updates into the existing set from another set.

# Example 1 - using difference() :-
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Seoul", "Kabul", "Delhi"}
# print(cities.difference(cities2))
# print(cities) # cities is not update


# Example 2 - using difference_update() :-
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities.difference_update(cities2)
print(cities) # cities is also updated
