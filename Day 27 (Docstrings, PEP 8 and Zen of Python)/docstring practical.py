# Example 1 :-
def sum(num1, num2):
    '''Take two number input from user and return the sum of two numbers.'''
    return num1 + num2



print(sum.__doc__) # using __doc__ we are printing docstring.
print()
num1 = int(input("Enter Num1: "))
num2 = int(input("Enter Num2: "))
result = sum(num1, num2)

print(f"\nThe Sum of {num1} + {num2} = {result}")


# Example 2 :-
def display(name):

    print(f"Hello {name}")
    '''Take name from user and print using function'''



# this docstring will return None because it is declared after the function body.
# the rule is to declare docstring before function body or just after the function, method, class below.
print(display.__doc__)
name = input("Enter Your Name: ").title()
display(name)