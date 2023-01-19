# if you want to append in a file.
# we use 'append' mode by using (a).
# Example :-
# Always open a file first, whenever you want to read, write or append.
# 'a' mode also create a file if the file is not exist.
f = open("newfile.txt","a") # we have already created a newfile.txt

f.write("\n\nHello Guys, I hope you understand basics of File Handling")

# now close a file
f.close()



# now read a file
f = open("newfile.txt","r") 

# print the content of file.
print(f.read())

# now close a file
f.close()