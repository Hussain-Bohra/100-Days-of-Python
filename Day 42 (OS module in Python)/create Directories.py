import os


# if not exists then create a directory.
if(not os.path.exists("data")):
    os.mkdir(f"data")
    

for i in range(1, 101):
    os.mkdir(f"data/mydata {i}")
    

