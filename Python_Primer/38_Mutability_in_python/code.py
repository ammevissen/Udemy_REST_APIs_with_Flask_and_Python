a=[]
b=a

print(id(a)) #id gives location in memory
print(id(b))

a.append(35)
print(a)
print(b)

a=[]
b=[] #new list
print(id(a)) #id gives location in memory
print(id(b))

a.append(35)
print(a)
print(b)

a=8597
b=8597
print(id(a))
print(id(b))
a=8599
print(id(a)) #ids are now different
print(id(b))

a="hello"
b=a

print(id(a))
print(id(b))

a=a+" world"
print(a)
print(b)
print(id(a))
print(id(b))