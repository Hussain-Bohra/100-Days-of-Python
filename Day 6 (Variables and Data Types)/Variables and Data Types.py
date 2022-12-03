# A Variable is like a container that holds data. Very similar to how our containers in kitchen holds sugar, salt etc. Creating a variable is like creating a placeholder in memory and assigning it some value.

# Declaration and Initialization of Variables :-
number = 24
name = "Brock Lesnar" 
isTrue = True
complexNumber = complex(2, 8)
pointNumbers = 19.57


# Data type specifies what type of value stored in a variable. This is required in programming to do various operations without causing an error.

# To Check the type of Variables we Declared above :-
# We use type() function :-
print("The type of \'number\' variable is: ", type(number))
print("\nThe type of \'name\' variable is: ", type(name))
print("\nThe type of \'isTrue\' variable is: ", type(isTrue))
print("\nThe type of \'complexNumber\' variable is: ", type(complexNumber))
print("\nThe type of \'pointNumbers\' variable is: ", type(pointNumbers))



# By default, Python provides the following built-in data types:
# 1. Numeric data type :- 
# a) int - an integer is a whole number, it can be positive as well as negative.
# Example - 4, -2, 0

# b) float - an floating number is a number which has decimal point value
# Example - 12.4, 9.6, 3.14


# 2. Text data type :-
# str - str stands for String, it is a set of characters which enclosed in double quotes.
# Example - "Hello World", "Python Programming", "Coders are Game Changer"


# 3. Boolean data type :-
# Boolean data consists of values True or False.



# 4. Sequenced data type :-
# a) list - A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets. Lists are mutable and can be modified after creation.
# Example - list = [3, 2.4, "Python", "Awesome"]

# b) tuple - A tuple is an ordered collection of data with elements separated by a comma and enclosed within parentheses. Tuples are immutable and can not be modified after creation.
# Example - tuple = ("Apple", "Banana", 245, 3.14)



# 5. Mapped data: dict
# dict - A dictionary is an unordered collection of data containing a key:value pair. The key:value pairs are enclosed within curly brackets.
# Example - dict1 = {"name":"John", "age":30}