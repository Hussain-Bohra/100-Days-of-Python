# Syntax :-
# if(condition):
#     if(condition2):
#         statement
#     else:
#         statement

# else:
#     statement


# Example :-
name = input("Enter Your Name: ")
if(name == "john"):
    age = int(input("Enter Your Age: "))

    if(age == 50):
        print()
        print("Details Matched:")
        print("Name is: ", name)
        print("Age is: ", age)

    else:
        print()
        print("Only Names are Matched:")
        print("Age is Different")

else:
    print()
    print(name,"Not Found in Our Database")

