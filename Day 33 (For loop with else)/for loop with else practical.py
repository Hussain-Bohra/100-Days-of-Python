# for loop with else :-
# Example :-
for i in range(1,6):
    print(i)

else:
    # after printing all the values, the else statement will also executed.
    print("Program Ends")

    


# for loop with else and break statement :-
# Example :-
for i in range(1,11):
    print(i)
    if(i == 7):
        # by using 'break' statement it will break the loop.
        break

else:
    # because of 'break' statement the 'else' statement will not be execute.
    print("Program Ends")

