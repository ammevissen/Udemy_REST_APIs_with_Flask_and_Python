class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def __str__(self): #magic method, called when you want to turn your object to a string
        return f"Person {self.name}, {self.age} years old."

    def __repr__(self): #magic method, can also be called when you turn your object to a string, but the purpose is for debugging.  To be able to easily recreate the object.
        return f"<Person('{self.name}', {self.age})>"
        

bob =Person("Bob", 35)
print(bob)