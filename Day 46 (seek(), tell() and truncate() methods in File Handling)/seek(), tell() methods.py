# Example of seek() :-
with open("myfile.txt","r") as f:
    # move the cursor position to the 8th character or byte
    f.seek(8)

    # contents = f.read() # it reads all contents after the 8th character
    contents = f.read(11) # it reads till 11 characters after the seek position of 8th character.
    print(contents)



# Example of tell() :-
with open("myfile.txt","r") as f:
    # move the cursor position to the 5th character or byte
    f.seek(5)

    # tell() methods return the position of our cursor in bytes.
    # it helps to track our cursor in which position it is currently.
    print(f"The Position of our cursor is (in Bytes): {f.tell()}")











