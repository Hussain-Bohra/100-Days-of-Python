# Parameterized Constructor Example :-
class Person():
    # __init__ is a special method that allows us to create a constructor.
    def __init__(self, name, occupation):
        # this method is automatically invoked at the runtime of creating objects.
        print("Method Invoked")
        self.name = name
        self.occupation = occupation


    def info(self):
        print(f"My Name is {self.name} and I am a {self.occupation}.")




# creating an object of class 'Person'.
obj1 = Person("Aditya","Teacher")
# now calling an 'info' method of 'Person' class.
obj1.info()

# creating another object of class 'Person'.
obj2 = Person("Prakash","Software Developer")
# now calling an 'info' method of 'Person' class.
obj2.info()
