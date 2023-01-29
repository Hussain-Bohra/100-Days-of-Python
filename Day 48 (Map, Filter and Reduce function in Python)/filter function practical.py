# declaring a function that return those numbers that greater than 5
def filter_function(num):
    return num > 5


# declaring and initializing a list
mylist = [20, 6, 2, 10, 3, 4]

# filter() takes two arguments :-
# 1st is a function, and 2nd is an iterable object whether it can be a list, tuple or dictionary.
result = list(filter(filter_function, mylist))

# We can also pass lambda function in filter()
result1 = list(filter(lambda num: num > 5, mylist))

print(f"Numbers that is Greater than 5 are: {result}")
print(f"Numbers that is Greater than 5 are: {result1}")

