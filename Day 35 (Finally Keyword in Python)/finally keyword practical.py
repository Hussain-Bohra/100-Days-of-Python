# try-catch block with finally keyword :- 
# Example :-
# try:
#     num = int(input("Enter a valid Number: "))

# except:
#     print("You have Entered Invalid Number!")

# finally:
#     print()
#     print("Program Execution Ended")


# As you can see in above example, irrespective of the condition the finally block will always be executed.


# Many times in a interview a question can be asked what is the use of finally keyword when we can also print any statement after try-catch completes their execution.
# Example :-
# try:
#     num = int(input("Enter a Valid Number: ")) 

# except:
#     print("Not a Valid Number!")

# this print statement will always execute because it is written outside the try-catch block, then what is the use of finally keyword?. 
# print("Program Ends!")


# so the answer of the interview question is, the use of finally keyword is important when we use functions. 
# Example :-
def myFunction():
    try:
        num = int(input("Enter a Valid Number: ")) 
        return True

    except:
        print("Not a Valid Number!")
        return False

    finally:
        # even the control goes back to the function calling, but this block will always executed.
        print("I am always Executed")


result = myFunction()
print(f"is_Number Valid: {result}")



