# Example 1: Function Without Parameters
def showHello():
    print("Hello World")


# We can Call Functions many time as we want.
showHello()
showHello()
showHello()


# Example 2: Function using Parameters
def printName(myname):
    print("Hello",myname)


# We can Call Functions many time as we want.
printName("Brock") # passing value at the time of calling function
printName("John") # passing value at the time of calling function
printName("Roman") # passing value at the time of calling function


# Since empty code is not allowed in python functions, if-else statements, loops etc.
# for that reason we have to use 'pass' keyword.
# the 'pass' statement is used as a placeholder for future code.
# Example :-
def myName():
    # if we do not define pass statement then our program will give an error.
    pass