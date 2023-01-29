# declaring a function that returns a cube of a number.
def cube(num):
    return num * num * num


# declaring and initializing a list[]
list_of_numbers = [2, 4, 1, 3, 5]

# map() takes two arguments :-
# map(function, any iterable object like (list,tuple or dictionary))

# here we are passing two arguments
# 1st is function and 2nd is list
result = list(map(cube, list_of_numbers))

# We can also pass lambda function in map()
result1 = list(map(lambda num: num * num * num, list_of_numbers))

print(f"Return cube of each elements from the list: {result}")
print(f"Return cube of each elements from the list: {result1}")