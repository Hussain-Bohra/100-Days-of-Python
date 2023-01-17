x = 5 # global variable

def myVariables():

    # to modify the global variable within function, we use global keyword.
    global x
    
    print(f"The value of global variable x is: {x}")  # x is a global variable, it can be accessible from anywhere in the program.
    
    x = 20 # now x is modified
    y = 10 # local variable
    print(f"The value of local variable y is: {y}") # y is a local variable, it cannot be accessible from outside the function.


myVariables()

print(f"The value of global variable x is: {x}") 