# 1. update() :-
# The update() method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.

# Example :-
# mydictionary1 = {"Name": "John Cena", "Age": 48, "HollyWood_Star": True}
# print(mydictionary1) 

# Updating the Existing Key:Value in 'mydictionary1'.
# mydictionary1.update({"Name": "Dwayne Johnson"})
# print(mydictionary1)

# Adding a new Key:Value in 'mydictionary1'.
# mydictionary1.update({"NickName": "The Rock"})
# print(mydictionary1)


# 2. clear() :-
# The clear() method removes all the items from the dictionary.

# Example :-
# mydictionary2 = {"Name": "Aman", "Gender": "Male", "Age": 20, "Smart": True} 
# print(mydictionary2)

# Removing all the items from mydictionary2.
# mydictionary2.clear()
# print(mydictionary2)



# 2. pop() :-
# The pop() method removes the key-value pair whose key is passed as a parameter.
# It removes only one key:value pair

# Example :-
# mydictionary3 = {"Name": "Rio", "Gender": "Male", "Age": 23, "Hacker": True} 
# print(mydictionary3)

# Removing one key from mydictionary3.
# mydictionary3.pop("Age")
# print(mydictionary3)



# 3. popitem() :-
# The popitem() method removes the last key-value pair from the dictionary.

# Example :-
# mydictionary4 = {"Name": "Sneha", "Gender": "Female", "Hacker": True} 
# print(mydictionary4)

# Removing last key from mydictionary4.
# mydictionary4.popitem()
# print(mydictionary4)



# 4. del :-
# we can also use the del keyword to remove a dictionary item.

# Example :-
mydictionary5 = {"Student1": "Karan", "Student2": "Shubham", "Student3": "Aashish"}
print(mydictionary5)


# Removing one key from mydictionary3.
del mydictionary5["Student1"]
print(mydictionary5)


# if We do not provide any key it will delete the whole dictionary. 
del mydictionary5

print(mydictionary5) # Now it will give a  NameError: name 'mydictionary5' is not defined.

