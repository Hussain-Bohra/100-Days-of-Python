import os

# Quick Quiz - Create a directory and its sub-directories, input the name of directory from user.
dirname = input("Enter Directory Name: ")

# check if the directory is already exists.
# if not exists then create a new directory.
if(not os.path.exists(dirname)):
    os.mkdir(f"{dirname}")
    

subDirName = input("Enter Sub-Directory Name: ")
for i in range(1, 101):
    # Creating 100 sub-Directories :-
    os.mkdir(f"{dirname}/{subDirName} {i}")
    

