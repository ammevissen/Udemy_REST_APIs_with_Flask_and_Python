numbers=[1, 3, 5]
double=[num*2 for num in numbers]

#most languages:
# for num in numbers:
#     double.append(num*2)

print(double)


friends=["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s=[friend for friend in friends if friend.startswith("S")]
starts_s2=[friend for friend in friends if friend.startswith("S")]

# for friend in friends:
#     if friend.startswith("S"):
#         starts_s.append(friend)

print(starts_s)

print(starts_s is starts_s2)
#id is memory locations
print("friends: ", id(friends), "Starts with 's'", id(starts_s), "Starts with 's' 2", id(starts_s2), )