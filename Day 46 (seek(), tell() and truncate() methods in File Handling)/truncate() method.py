# Example of truncate() :-
with open("sample.txt","w") as f:
    f.write("Hello World")
    # it remove all the contents after 5th character or byte
    f.truncate(5)


with open("sample.txt","r") as f:
    print(f.read())