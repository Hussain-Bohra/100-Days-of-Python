# I am using 'with' statement so that it automatically close a file.

# Example 1 of writelines() method
# create a file1.txt and open it in 'write' mode.
with open("file1.txt","w") as f:

    # writing in a file using a list of strings :-
    lines = ["Python\n", "is\n", "an Awesome\n", "Programming\n", "Language"]
    f.writelines(lines)



# Example 2 of writelines() method
# create a file2.txt and open it in 'write' mode.
with open("file2.txt","w") as f:

    # writing in a file using a multi line strings :-
    lines = '''Hello This is to inform you
that you are doing great.
I hope you will remain your consistency 
till the 100 days of Code in Python.'''
    f.writelines(lines)