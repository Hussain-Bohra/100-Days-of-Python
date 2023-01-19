# to create a file only,
# we use 'x' mode.
# Example :-
# if the file is already exist then it will throw an FileExistsError.
f = open("main.py","x") # this will create main.py file.


f.close()