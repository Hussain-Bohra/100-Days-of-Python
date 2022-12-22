# Tuple Declaration and Initialization :-
# storing numbers in a tuple
tup1 = (1, 2, 3, 4, 5)
print(tup1)

tup2 = ("John", "Brock", "Austin", "Rock")
# storing strings in a tuple
print(tup2)


# storing different data type values in a tuple
tup3 = ("Green", "Red", "Blue", 1, 2, True)
print(tup3)


# if we store only one value in tuple then python will consider it as a list.
# for that solution we have to use comma(,)
# Example 1 :- without using comma(,)
tup4 = (1)
print(type(tup4)) # it consider as int
tup5 = ("Hello")
print(type(tup5)) # it consider as string

# Example 2 :- after using comma(,)
tup6 = (1,)
print(type(tup6)) # it consider as tuple
tup7 = ("Hello",)
print(type(tup7)) # it consider as tuple



# Access tuple using it's index no :-
# Positive Index Example
# positive index starts from 0(Zero)
mytuple = ("Oranges", "Mangoes", "Apples", "Watermelon")
# indexno       0         1          2           3
print(mytuple[0])
print(mytuple[1])
print(mytuple[2])
print(mytuple[3])
# print(mytuple[4]) # it will give index out of range error



# Negative Index Example
# negative index starts from -1
colors = ("Yellow", "Black", "Red", "Blue", "Cyan")
# indexno    -5       -4      -3     -2      -1
print(colors[-1])
print(colors[-3])
print(colors[-5])
# print(colors[-7]) # it will give index out of range error



# Check if the item is present in a tuple or not.
# using 'in' keyword
countries = ("Germany", "England", "Australia", "India", "Japan")
if "India" in countries:
    print("India is Present!")
else:
    print("India is not Present!")




# Print Elements using Range of Indexes.
# Syntax: (starting_no, ending_no, jump_no)
# Example 1: using positive index no
newtuple = ("Red", "Green", "Blue", "Yellow", "Orange", "Cyan", "Purple")
# indexno     0       1       2         3         4        5        6

print(newtuple[3 : 5]) # print elements from 3 to 4 that is 5-1.
print(newtuple[2 : 6]) # print elements from 2 to 5 that is 6-1.



# Example 2: using negative index no
print(newtuple[-4 : -2]) # print elements from len(newtuple) - 4 to len(newtuple) - 2 that is 3 to 5, as last no will not included so it will print till 4 .
print(newtuple[-5 : -3]) # print elements from len(newtuple) - 5 to len(newtuple) - 3 that is 2 to 4, as last no will not included so it will print till 3 .



# Example 3: print alternate values by providing jump index no
print(newtuple[0 : 7 : 2])
print(newtuple[0 : 7 : 3])





