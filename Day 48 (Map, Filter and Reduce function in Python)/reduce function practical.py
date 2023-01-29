# to use reduce function, we need to import it from 'functools' module.
from functools import reduce

# declaring and initializing a list of numbers
mylist = [2, 4, 6, 8]

# calculate the sum of the numbers using reduce function.
result = reduce(lambda x,y: x + y, mylist)

print(result)