# 1. count()
# Returns the count of the number of items with the given value.
# Example :-
# list1 = [1, 2, 1, 3, 1, 5]
# print("How Many Times 1 Appear in a list: ",list1.count(1))



# 2. sort()
# Example :-
# list2 = [5, 1, 2, 3, 7, 6, 4, 10, 8, 9]
# print("Original List: ",list2)
# list2.sort()
# print("Sort in Ascending Order: ",list2)
# list2.sort(reverse=True)
# print("Sort in Descending Order: ",list2)



# 3. index()
# This method returns the index of the first occurrence of the list item.
# Example :-
# list3 = ["Orange", "Apple", "Mango", "Banana", "Guava", "Mango"]
# index     0         1         2         3         4        5
# print("Indexno of Mango is: ",list3.index("Mango"))



# 4. reverse()
# This method reverses the order of the list.
# Example :-
# list4 = [3, 2, 1, 4, 5]
# print("Original list:",list4)
# list4.reverse()
# print("Reversing the list:",list4)



# 5. append()
# This method appends items to the end of the existing list.
# Example :-
# list5 = ["John", "Kevin", "Roman"]
# print("Original list:",list5)
# list5.append("Paul")
# print("Adding Paul:",list5)



# 6. insert()
# This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.
# Example :-
# list6 = ["John", "Lita", "Becky", "Alexa"]
# print("Original list:",list6)
# list6.insert(1,"Brock")
# print("Modified list:",list6)



# 7. copy()
# Returns copy of the list. This can be done to perform operations on the list without modifying the original list.
# Example 1 :- without copy() method
# originalList1 = [1, 2, 3, 4, 5]
# copyList1 = originalList1
# The original list will also change by modifiying copied list.
# copyList1[0] = 44
# print(originalList1)
# print(copyList1)


# Example 2 :- using copy() method
# originalList2 = [1, 2, 3, 4, 5]
# The original list will not change, because of using copy() method.
# copyList2 = originalList2.copy()
# print(originalList2)
# print(copyList2)



# 8. extend()
# This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.
# Example 1 :- Concatenate List Using Extend() method
color1 = ["Red", "Green", "Blue"]
color2 = ["Black", "Cyan", "Yellow"]
color1.extend(color2)
print("Concatenate list using extend():",color1)


# Example 2 :- Concatenate Without Using Extend() method
color1 = ["Red", "Green", "Blue"]
color2 = ["Black", "Cyan", "Yellow"]
color3 = color1 + color2
print("Concatenate List Without extend():",color3)


