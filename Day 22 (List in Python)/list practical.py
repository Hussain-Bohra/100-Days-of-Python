# list example :-
# Example 1 : storing same type of elements.
# here we storing integers only.
# list1 = [4, 5, 1, 2, 3]
# print(list1)



# Example 2 : storing different type of elements.
# here we storing string, boolean, integer, and floating numbers.
# list2 = ["Hello", True, 2, 4.4]
# print(list2)



#************************************************************************
# Indexing of List :-
# in list, index starts with zero 0
# a) Positive Indexing :-
# fruits = ["Orange", "Mango", "Banana", "Guava", "Apple"]
# print(fruits[0]) # print Orange
# print(fruits[1]) # print Mango


# b) Negative Indexing :-
# it works in reverse order, that is it starts from -1, -2 ,-3 and so on.
# Always Remember this Formula: it always use the length of your list, so subtract the negative index from the length of your list, you will get the answer.
# print(fruits[-3]) # print Banana
# print(fruits[len(fruits)-3]) # print Banana



# Check whether an item is present in the list or not?
# using the in keyword
# list3 = ["John", "Bray", "Cole", "Brock"]

# if "Brock" in list3:
#     print("Yes, Brock is Already Added in Your List")

# else:
#     print("Not Available")
        

# Range of Index :- 
# colors = ["Red", "Green", "Blue", "Cyan", "Black", "White"]

# We can print the elements within a particular range.
# print(colors[1:4]) # it will print from 1 to 4-1 that is 3rd number of element.
# print(colors[2:-2]) # Remember the Formula.
# print(colors[:]) # if we do not provide index number it will print all elements by default.
# print(colors[:4]) # we can also define only end index number.
# print(colors[::2]) # we can also define jump values also.
#************************************************************************


# List Comprehension :-
# We can also perform conditional statements in list
# Example 1 :-
names = ["Brock", "John", "Roman", "Rock", "Vince"]
newlist = [item for item in names if "k" in item]
print("Display Only those Names that endswith 'k': ",newlist)




# Example 2 :-
names = ["Brock", "John", "Roman", "Rock", "Vince"]
newlist = [item for item in names if (len(item) > 4)]
print("Display Only those Names that have more than 4 letters: ",newlist)






