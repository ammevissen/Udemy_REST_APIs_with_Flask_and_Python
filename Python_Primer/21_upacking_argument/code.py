from typing import TextIO


def multipy(*args):
    print(args)
    total=1
    for arg in args:
        total*=arg
    return(total)

print(multipy(1,3,5))

def add(x, y):
    return x+y

nums=[3, 5]
print(add(*nums)) #passes one value per variable, they need to be the same length 

nums={"x":15, "y":25}
print(add(x=nums["x"], y=nums["y"]))
#since variables (in add function) are the same as keys can do:
print(add(**nums))

#creates a required named operator:
def apply(*args, operator):
    if operator=="*":
        return(multipy(*args))
    elif operator=="+":
        return(sum(args))
    else:
        return("No valid operator provided to apply().")

print(apply(1, 3, 6, 7, operator="+"))
print(apply(1, 3, 6, 7, operator="*"))
