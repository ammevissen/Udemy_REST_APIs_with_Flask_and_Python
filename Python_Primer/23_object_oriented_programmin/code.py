student={"name": "Rolf", "grades":(89, 90, 93, 78, 90)}

def average(sequence):
    return sum(sequence)/len(sequence)

print(average(student["grades"]))
#want to be able to call:
# print(student["grades"].average())