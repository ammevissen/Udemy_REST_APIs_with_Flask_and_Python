# def named(**kwargs): #keyword arguments
#     print(kwargs)

# named(name="Bob", age=25) #prints a dictionar

def named(name, age):
    print(name, age)

details={"name": "Bob", "age":25}
named(**details)

#**used to collect into a dictionary in the function description or to unpack the dictionary to keyword arguments in the function call

def print_nicely(**kwargs):
    named(**kwargs) #print the dictionary
    for arg, value in kwargs.items(): #iterate over the dictionary
        print(f"{arg}: {value}")

print_nicely(name="Bob", age=25)

#collects positional arguments into args, and all of the keyword arguments into kwargs
def both(*args, **kwargs): #Can add an unlimited number of arguments
    print(args)
    print(kwargs)

both(1, 3, 5, name="Bob", age=25)

def myFunction(**kwargs):
    print(kwargs)

#Will return error.
# myFunction(**"Bob") #Error, must be mapping
# myFunction(**None) #Error
