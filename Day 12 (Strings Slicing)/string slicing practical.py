# find the length of the string using len() function.
# Example 1 :-
# name = "Mango"
# print(len(name))

# Example 2 :-
# myname = "Mango"
# mynameLen = len(name) 
# print("The Length of",myname,"is: ",mynameLen)


# String Slicing Example :-
# Syntax - print(str[start_index_no:ending_index_no])
# We already know string can be access by its index numbers and that number start from zero 0.

str = "Hello"
# print(str[0:3])     # this print Hel, because it start from 0, but stop at 2, not 3. 
# print(str[:3])      # if we do not specify starting range, it include zero by default. 

# print(str[0:len(str)-3])    # this print He, because it includes 0, but stop at 1, because length of Hello is 5 and 5-3 is 2, hence it will not stop at 2, it will stop at 1. 
# print(str[0:-3])    # you can also write above statement like this.


print(str[::-1])      # an awesome python trick to print string in reverse order.


