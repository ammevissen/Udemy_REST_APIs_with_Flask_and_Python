friends={"Bob", "Rolf", "Anne"}
abroad={"Bob", "Anne", "Chris"}


local_friends=friends.difference(abroad)

print(local_friends)
print(friends-abroad)

local_friends2=abroad.difference(friends)
print(local_friends2)


local_friends3=friends.union(abroad)
print(local_friends3)

art={"Bob", "Jen", "Rolf", "Charlie"}
science={"Bob", "Jen", "Adam", "Anne"}

both=art.intersection(science)
print(both)