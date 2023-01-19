# lambda function is a annonymous function, that means a function without name.

# Example 1 - lambda function with single argument :-
# Write a program to print a square of a number using lambda :-
# square = lambda num: num * num

# num = int(input("Enter Num: "))
# print(f"The Square of {num} is: {square(num)}")



# Example 2 - lambda function with multiple arguments :-
# Write a program to add two numbers using lambda :-
# addTwoNumbers = lambda num1,num2: num1 + num2

# num1 = int(input("Enter Num1: "))
# num2 = int(input("Enter Num2: "))
# result = addTwoNumbers(num1,num2)
# print(f"The Sum of {num1} + {num2} is: {result}")



# Example 3 - Passing lamda function as an argument :-
# In this example, we are creating a function using lambda and store it in a variable named cube. 
cube = lambda num: num * num * num

# now we are creating a basic function that returns 2 + cube of 3.
def myfunc(cubeof): # cubeof is just a name of parameter.
    return 6 + cubeof(3) # 6 + 27 that is 3*3*3=27


# now we are passing cube function as an argument to the parameter of -> myfunc(cubeof).
result = myfunc(cube) # passing cube function as an argument and store returning value in a 'result' variable.

print(result) # it prints 33
