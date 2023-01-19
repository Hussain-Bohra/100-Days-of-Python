# I am using 'with' statement so that it automatically close a file.

# Examples of readline() method :-
# readline() method reads a single line only from a file.
# reading a file1.txt file :-
with open("file1.txt", "r") as f:
    print(f.readline()) # returns only first line of a file.


# reading a file2.txt file :-
with open("file2.txt", "r") as f:
    print(f.readline()) # returns only first line of a file.



# Examples of readlines() method :-
# readlines() method read all contents of a file and return it as a list of strings.
# reading a file1.txt file :-
with open("file1.txt", "r") as f:
    print(f.readlines()) # returns all contents as a list of strings


# reading a file2.txt file :-
with open("file2.txt", "r") as f:
    print(f.readlines()) # returns all contents as a list of strings
