class ClassTest:
    def instance_method(self): #funtion, uses self.  All methods that use self as first parameter are instance methods.  Used for most things.  Do action that uses/modifies the data inside of the class.
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls): #usually use cls.  Class is passed in as argument.  Used as a factory 
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method(): #does not have self or cls.  Really just a function inside of a class, but doesn't use the class.  Rarely used
        print("Called static_method")


test=ClassTest() #don't need an __init__ method..just means no need to initialize anything
# test.instance_method()
# ClassTest.instance_method(test)

ClassTest.class_method()

ClassTest.static_method()