# Declaration and Initialization :- 
mydictionary = {"Name": "Brock", "Age": 45, "isBeast": True}
print(mydictionary)


# Accessing Single Value :-

print(mydictionary.get("Name")) # if we use get(), it will result 'None' if the value is not present in the dictionary.
print(mydictionary["Age"]) # but if we use this method then it will give an error, if value is not present in the dictionary.


# Accessing Multiple Values :-
print(mydictionary.values())


# Accessing Keys only :-
print(mydictionary.keys())


# Accessing Key:Value Pairs :-
print(mydictionary.items())



# Accessing keys using for loop :-
# Accessing keys using for loop :-
for key in mydictionary.keys():
    print(f"Keys are: {key}")



# Accessing key:value pairs using for loop :-
for key, value in mydictionary.items():
    print(f"The value of the corresponding {key} is: {value}")






