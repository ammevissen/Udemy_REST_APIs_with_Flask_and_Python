def add(x, y):
    result=x+y
    return(result)


print(add(5, 3))


# def say_hello():
#     print("Hello!")

#say_hello("Bob")  #Will return an error since say_hello doesn't take any parameters



def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Bob") #if don't include an argument will return an error

def say_hello2(name, surname):
    print(f"Hello, {name} {surname}!")

say_hello2(surname="Bob", name="Smith")