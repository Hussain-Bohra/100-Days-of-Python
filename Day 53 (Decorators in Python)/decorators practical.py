# Example 1 :-
# defining the decorator_function :-
# def decorator_function(hello):
#     def myfunc():
#         print("Good Morning Sir.")
#         hello()
#         print("Thanks for Using Sir.")
#     return myfunc


# @decorator_function
# def hello():
#     print("Hi I am Hello Function!")

# Function calling :-
# hello()


# Example 2 :-
# defining the decorator_function :-
def decorator_function(add_two_numbers):
    def displayMessage(*args, **kwargs):
        print("Hello User :-")
        add_two_numbers(*args, **kwargs)
        print("Thanks for using Calculator :-")
    return displayMessage

# to use method 1 to call this decorator_function, we need to define it on above of the function using @
# @decorator_function
def add_two_numbers(num1, num2):
    print(f"Sum of {num1} + {num2} is: {num1 + num2}")


# method 1 to call a decorator_function :-
# add_two_numbers(6, 10)

# method 2 to call a decorator_function :-
# if we use this method then there is no need to define it using the @.
decorator_function(add_two_numbers)(6, 10)