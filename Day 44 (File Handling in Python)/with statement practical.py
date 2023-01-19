# we know that everytime we open a file, then we have to close a file also.
# but this becomes little time consuming.
# but because of 'with' statement there is no need to remember now, to close a file.
# with statement automatically close a file.
# Syntax :-
# here we use as keyword to give an alternative name.
# with open("filename","mode") as aliasName:
    # statements
    # statements


# Example :-
with open("notebook.txt","a") as f:
    f.write("Hello This is your Notebook")
    f.write("\nYou can Write here what you have learned")
    f.write("\nTill Now")