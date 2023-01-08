# enumerate function :-
# Example - using list[] :-
# mylist1 = ["Shubham", "Aditya", "Jatin", "Hitesh"]

# for index, names in enumerate(mylist1):
#     print(f"{index}: {names}")


# by default, index number start from 0.
# you can change this number by using "start" parameter.
# Example :-
# mylist2 = ["Ashish", "Rohan", "Vijay", "Arjun"]
# for index, names in enumerate(mylist2, start=5):
#     print(f"{index}: {names}")





# Example - using tuple() :-
# mytup = ("John", "Brock", "Kevin", "Roman")

# for index, names in enumerate(mytup):
#     print(f"{index}: {names}")



# Example - using string :-
mystr = "Hello"

for index, names in enumerate(mystr, start=1):
    print(f"{index}: {names}")

