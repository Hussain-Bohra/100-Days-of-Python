import os

# list all directories stored in data. 
folders = os.listdir("data")

print(folders)

for folder in folders:
    print(folder)

