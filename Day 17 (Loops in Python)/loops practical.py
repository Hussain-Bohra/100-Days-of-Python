# for loop Example :-
# Iteration over a string :-
# str = "john"
# for st in str:
    # print(st)


# Iteration over a list :-
# fruits = ["Apple", "Orange", "Mango", "Banana"] 
# for ft in fruits:
    # print(ft)
    # We can also use nested loops like this
    # for i in ft:
        # print(i)


# range() function to iterate numbers :-
# range() takes three parameters :-
# range(start_no, stop_no, increment_no)
# Note: range() iterate till n-1, for example if you specify range(5) it will start from 0 and stop at 4, not 5.
# Example 1 :-
# for num1 in range(5): # if we do not specify start no, it takes 0 by default.
    # print(num1)


# Example 2 :-
# for num2 in range(1,10): # here number starts from 1 and stop at 9.
    # print(num2)


# Example 3 :-
for num3 in range(1,11,3): # you can also specify the increment number.
    print(num3) 
