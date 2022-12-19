# 1. Default Argument Example :-
# def printName(firstName, lastName="Lesnar"):

    # print("Hello,",firstName, lastName)


# function calling
# printName("Brock")
# printName("John","Cena")



# 2. Keyword Arguments Example :-
# def details(name, age):
    # print("Your Name:", name)
    # print("Your Age:", age)


# function calling
# details(age=30, name="John")
# details(name="Lita", age=50)




# 3. Required Arguments Example :-
# def fullDetails(name, age, city):
    # print("Name: ",name) 
    # print("Age: ",age) 
    # print("City: ",city) 


# function calling
# fullDetails("John",50) # passing only 2 arguments out of 3 will give an error
# fullDetails("John", 50,"Boston")




# 4. Variable Length Arguments Example :-
# a) Arbitrary Arguments :-
# def numbers(*numbers):
    # print(numbers[0])
    # print(numbers[1])
    # print(numbers[2])



# function calling
# We can pass any number of arguments.
# numbers(1, 2, 3)



# b) Keyword Arbitrary Arguments :-
# it is just a key=value pair.
# def listOfNames(**multipleNames):
#     print("Name1: ", multipleNames["name1"])
#     print("Name2: ", multipleNames["name2"])
#     print("Name3: ", multipleNames["name3"])



# function calling
# listOfNames(name1 = "Leo", name2 = "Alina", name3 = "Dwayne")




# return statement Example :-
def add(a, b):
    return a + b # first add the numbers and then return the value to the function call.


# function calling
result = add(5, 15) # get the value and store it in a 'result' variable.
print("Sum of a + b is:",result)