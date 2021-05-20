def add(x, y=8): #cannot have a default parameter before non default parameters
    print(x+y)

add(5)
add(x=5)
add(x=5, y=5)

#don't do:
default_y=3
def add2(x, y=default_y):
    print(x+y)


add2(2)

default_y=4 #default in the function is still 3...is confusing.  
add2(2)