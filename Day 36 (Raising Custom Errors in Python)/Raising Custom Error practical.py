# Example 1 :-
# salary = int(input("Enter salary amount: "))
# if not 2000 < salary < 5000:
#     raise ValueError("Not a valid salary")

# Example 2 :-
# num = int(input("Enter a Number Between 5 to 9: "))
# if (num < 5 or num > 9):
#     raise ValueError("Entered Number is not between 5 to 9!")



# Quick Quiz - When user enter 'quit' in lowercase then terminate the program else raise an error.
# Solve Quick Quiz :-
# Example 1 :-
# num = input("Enter a Number Between 5 to 9: ")

# if (num == "quit"):
#     pass
    
# elif (int(num) < 5 or int(num) > 9):
#         raise ValueError("Entered Number is not between 5 to 9!")



# Example 2 :-
num = input("Enter a Number Between 5 to 9: ")

if "quit" in num:
    pass
    
elif (int(num) < 5 or int(num) > 9):
        raise ValueError("Entered Number is not between 5 to 9!")
