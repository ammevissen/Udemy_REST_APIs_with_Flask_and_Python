# def add(x, y):
#     return (x+y)

#lambda:
    #lambda, variables, colon, return
add=lambda x, y: x+y

print(add(5, 8))

def double(x):
    return x*2

sequence=[1, 3, 5, 9]

#same thing:
doubled=[double(x) for x in sequence] #usually slightly faster
print(doubled)

doubled=list(map(double, sequence)) #syntax is more similar other laguages (which other devs on your team may be familiar with)
print(doubled)

doubled=list(map(lambda x:x*2, sequence))
print(doubled)

doubled=[(lambda x: x*2)(x) for x in sequence]
print(doubled)

