# short hand if-else statment :-
# Example :-
# num1 = int(input("Enter Num1: "))
# num2 = int(input("Enter Num2: "))

# print(f"{num1} is Greater") if num1 > num2 else print(f"{num2} is Greater")




# short hand if-else with multple else statments :-
# Example :-
# num1 = int(input("Enter Num1: "))
# num2 = int(input("Enter Num2: "))

# print(f"{num1} is Greater") if num1 > num2 else print(f"Both are Equal") if num1 == num2 else print(f"{num2} is Greater")




# we can also store ouput in a variable :-
# Example :-
num1 = int(input("Enter Num1: "))
num2 = int(input("Enter Num2: "))

result = f"{num1} is Greater" if num1 > num2 else f"Both are Equal" if num1 == num2 else f"{num2} is Greater"

print(result)




