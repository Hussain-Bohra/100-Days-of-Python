# creating a class
# using class keyword
# Example 1 :-
class Details:
    name = "Brock"
    age = 40



# creating an object of 'Details' class.
obj = Details()
print(f"Name is: {obj.name}")
print(f"Age is: {obj.age}")


# Example 2 - self parameter
class MyDetails():
    name = "Roman Reigns"
    occupation = "Wrestler"

    # defining a function
    def showDetails(self):
        print(f"Name is {self.name} and Occupation is {self.occupation}.")


# creating an object of 'MyDetails' class.
obj1 = MyDetails()
obj1.showDetails()


# changing default values for a new object
obj2 = MyDetails()
obj2.name = "John"
obj2.occupation = "Software Developer"
obj2.showDetails()



