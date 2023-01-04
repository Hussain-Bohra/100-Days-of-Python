# try-catch block :-
# Example 1 :-
try:
    num = int(input("Enter a Valid Integer Number: "))

except:
    print("Number is not an Integer")



# Example 2 :-
try:
    num = float(input("Enter a Valid Float Number: "))


# We can also print the name of the error by using 'Exception' class.
except Exception as e:
    print(e)


