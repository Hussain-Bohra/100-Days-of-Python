# using from keyword we can import all or any specific function from a module :-
# Example 1 - import all function from a module :-
# from math import *


# Example 2 - import specific functions from a module :-
from math import factorial, fmod

num = int(input("Enter a Number: "))
print(f"\nThe factorial of {num} is: {factorial(num)}")


num1 = int(input("Enter Num1 : "))
num2 = int(input("Enter Num2: "))

print(f"The Remainder of {num1}/{num2}: {fmod(num1,num2)}")


# print(sqrt(26)) # this will throw an error because we have defined sqrt function in import statement.