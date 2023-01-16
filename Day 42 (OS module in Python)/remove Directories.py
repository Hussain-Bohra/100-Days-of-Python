import os


# Removing 100 Directories :-
for i in range(1, 101):
    # first - remove sub-directories
    os.rmdir(f"data/mydata {i}")

else:
    # second - then remove parent directory
    os.rmdir(f"data")
