# match case example :-
# Note: Match Case Statements only works in Python 3.10 version or above, so make sure to check your python version before running match case program.

# Create a week day program using match case :-
day_no = int(input("Enter Day No: "))
print()

match day_no:
    case 1:
        print("Day No is:",day_no)
        print("Day is Monday")
        
    case 2:
        print("Day No is:",day_no)
        print("Day is Tuesday")

    case 3:
        print("Day No is:",day_no)
        print("Day is Wednesday")

    case 4:
        print("Day No is:",day_no)
        print("Day is Thursday")

    case 5:
        print("Day No is:",day_no)
        print("Day is Friday")

    case 6:
        print("Day No is:",day_no)
        print("Day is Saturday")

    case 7:
        print("Day No is:",day_no)
        print("Day is Sunday")

    case _:
        print("You Have Entered Invalid Day No")
