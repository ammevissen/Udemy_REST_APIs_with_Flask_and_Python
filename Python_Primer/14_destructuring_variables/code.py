x=(5, 11)
y=5, 11 #also a tuple

t=5, 11
a, b=t
print(a, b)

student_attendance={"Rolf":96, "Bob":80, "Anne":100}

print(list(student_attendance.items()))

for t in student_attendance.items():
    print(t)

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

people=[("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

person=people[0]

# "_" don't care about variable, and is meant to be ignored
name, _, profession=person

head, *tail=[1, 2, 3, 4, 5]
print(head)
print(tail)

*head, tail=[1, 2, 3, 4, 5]
print(head)
print(tail)

