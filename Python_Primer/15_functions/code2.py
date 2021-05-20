#Things to avoid:
#reusing premade functions:

# def print():
#     print("Hello World!")

# print()

friends=["Rolf", "Bob"] 
def add_friend():
    friend_name=input("Enter your friend name: ")
    #friends=friends+[friend_name] #function scope for friends, it sees it is being definec in the same line that it is being used.  Called shadowing a variable
    #think x=x+5 (when x is not defined)
    f=friends+[friend_name] #is acceptable since f is being defined.  Python checks the function scope, does not see a friends variable, then it checks outside of the function scope.  It sees the friends variable and uses it.  

def add_friends2():
    friends2.append("Rolf")

friends2=[]
add_friends2()
add_friends2()
add_friends2()

print(friends2)