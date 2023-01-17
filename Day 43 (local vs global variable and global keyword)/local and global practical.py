x = 5 # global variable

def myVariables():

    y = 10 # local variable
    print(f"The value of global variable x is: {x}")  # x is a global variable, it can be accessible from anywhere in the program.
    print(f"The value of local variable y is: {y}") # y is a local variable


myVariables()
print(f"The value of local variable y is: {y}") # this will throw an error, because local variables can't be accessible outside the function.