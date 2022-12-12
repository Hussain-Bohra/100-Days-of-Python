# 1. upper()
# The upper() method converts a string to upper case.
# Example
str1 = "hello world"
print("uppercase: ",str1.upper())
print()



# 2. lower()
# The lower() method converts a string to lower case.
# Example
str2 = "hello world"
print("lowercase: ",str2.lower())
print()



# 3. strip()
# The strip() method removes any white spaces before and after the string (Not between the string).
# Example
str3 = "     hello world      "
print("Before removing white spaces: ",str3)
print("After removing white spaces (before and after the string): ",str3.strip())
print()



# 4. rstrip()
# Example
str4 = "hello world !!!!"
print("Before Removing trailing characters: ",str4)
print("After Removing trailing characters: ",str4.rstrip("!"))
print()



# 5. replace()
# The replace() method replaces all occurences of a string with another string.
# Example
str5 = "Hello john"
print("Replacing john with world: ", str5.replace("john","world"))
print()



# 6. split()
# The split() method splits the given string at the specified instance and returns the separated strings as list items.
# Example
str6 = "Hello world"
print("split the string at the white space: ", str6.split(" "))
print()



# 7. capitalize()
# The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.
# Example
str7 = "hello How Are yOU"
print(str7.capitalize())
print()



# 8. center()
# The center() method aligns the string to the center as per the parameters given by the user.
# Example 1
str8 = "Welcome to the 100 Days of Python"
print(str8.center(50))

# Example 2
# We can also provide padding character. It will fill the rest of the fill characters provided by the user.
print(str8.center(50,"."))
print()



# 9. count()
# The count() method returns the number of times the given value has occurred within the given string.
# Example
str9 = "ABCD abcd aBCD"
print(str9.count("a")) # there are three (a) right but it returns only 2 because it checks the character with its case also, so in this case python is returning the count of small (a) and capital (A) will be skip.
print()



# 10. swapcase()
# The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.
# Example
str10 = "HELLO world"
print("Converts UPPERCASE to lowercase and vice versa: ", str10.swapcase())
print()



# 11. find()
# The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is not present in the string then it return -1.
# Example
str11 = "he is Damien, and he is a Developer"
print(str11.find("is")) # it return the index number of first occurence of 'is' that is 3
print(str11.find("john")) # there is no "john" in the string, so that it returns -1
print()



# 12. index()
# The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.
# Example
str12 = "he is Damien, and he is a Developer"
print(str12.index("is")) # same as find() returns the index number of first occurrence of a given character.
# print(str12.index("john")) # in find() it returns -1, but in index() it returns an error.
print()



# 13. isalnum()
# The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other special characters or punctuations are present, then it returns False.
# Example
str13 = "abcdABCD012"
print(str13.isalnum())
print()



# 14. isalpha()
# The isalpha() method returns True only if the entire string consists a-z or A-Z only. else returns false.
# Example
str14 = "abcdABCD012"
print(str14.isalpha())
print()



# 15. islower()
# The islower() method returns True if all the characters in the string are lower case, else it returns False.
# Example
str15 = "hello how are you?"
print(str15.islower())
print()



# 16. upper()
# The isupper() method returns True if all the characters in the string are upper case, else it returns False.
# Example
str16 = "HELLO HOW ARE YOU?"
print(str16.isupper())
print()



# 17. isprintable()
# The isprintable() method returns True if all the values within the given string are printable, if not, then return False.
# Example 1
str17 = "We are learning strings methods"
print(str17.isprintable())

# Example 2
str17 = "We are learning\n strings methods"
print(str17.isprintable()) # using backslash characters consist not printable, so that it returns false.
print()



# 18. isspace()
# The isspace() method returns True only if the string contains white spaces, else returns False.
# Example 1
str18 = "   " # you can print spaces using spacebar or using tab key.
print(str18.isspace())

# Example 2
str18 = "  Hello "
print(str18.isspace()) # it returns false because the isspace() method says your string contains only white spaces and not any other characters, understood. 
print()



# 19. title()
# The title() method capitalizes each letter of the word within the string.
# Example
str19 = "welcome to the 100 days of python programming" 
print(str19.title())
print()



# 20. istitle()
# The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.
# Example 1
str20 = "Hello How Are You?"
print(str20.istitle())

# Example 2
str20 = "Hello How are you?"
print(str20.istitle())
print()



# 21. startswith()
# The startswith() method checks if the string starts with a given value. If yes then return True, else return False.
# Example
str21 = "Python is a interpreted language"
print("is str21 starts with Python?: ",str21.startswith("Python"))
print("is str21 starts with python?(Case is different): ",str21.startswith("python"))
print()



# 22. endswith()
# The endswith() method checks if the string ends with a given value. If yes then return True, else return False.
# Example
str22 = "Welcome to the 100 Days of Python Programming"
print("is str22 ends with Programming?: ",str22.endswith("Programming"))
# # Note: endswith() checks with case sensitive
print("is str22 ends with programming?(Case is different): ",str22.endswith("programming"))
print()