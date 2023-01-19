# to write a content in a file, first we need to open a file in 'write' mode.
# the advantage of using 'write' mode is, it will automatically create a file if the file is not exist on your system.
f = open("newfile.txt","w")

# one thing to remember is 'write' mode will overwrite the contents in a file.
f.write("Hello This is newfile, created using 'write' mode.")

f.close()

# now read a file
f = open("newfile.txt","r")
print(f.read())

f.close()