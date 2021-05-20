l=["bob", "Rolf", "Anne"]

t=("bob", "Rolf", "Anne")

s={"bob", "Rolf", "Anne"}

print(l[0])
print(t[2])

l[0]="Smith"
print(l[0])

l.append("Smith")

#cannot modify a tuple, either with index or append
print(l)
l.remove("Smith")
print(l)

s.add("Smith")
s.add("Smith")
print(s)
