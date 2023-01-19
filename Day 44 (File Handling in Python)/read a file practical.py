# Make sure the file is exist, otherwise this will throw an FileNotFound error.
# f = open("myfile2.txt","r") # this will throw an error because myfile2.txt is not exist
f = open("myfile.txt","r")

# reading a content from a file and print it on the screen.
contents = f.read()
print(contents)

# It is important to close a file after reading, this releases the resources used by a file.
f.close()