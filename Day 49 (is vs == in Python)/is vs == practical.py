# is checks if two object's values are same and also if they stored in the same memory, then it will return true.
# == checks if two object's values are same only, then it will return true.


# Example 1 - using integers :- 
a = 10
b = 10

print("Integer Comparison :-")
print(a is b)
print(a == b)
print()


# Example 2 - using strings :- 
str1 = "hello"
str2 = "hello"

print("Strings Comparison :-")
print(str1 is str2)
print(str1 == str2)
print()


# Example 3 - using list:- 
list1 = [1, 2, 3]
list2 = [1, 2, 3]

print("Lists Comparison :-")
print(list1 is list2)
print(list1 == list2)
print()


# Example 4 - using integer and string :-
a = 5
b = "5"

print("Integer and String Comparison :-")
print(a is b)
print(a == b)
print()


# Example 5 - using None :-
a = None
b = None

print("None Comparison :-")
print(a is None)
print(a == None)