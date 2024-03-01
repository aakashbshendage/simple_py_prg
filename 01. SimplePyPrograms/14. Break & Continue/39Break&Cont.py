students = ["Ram", "Shyam", "Kishan", "Radha", "Radhika"]

for student in students:
    if student == "Radha":
        break; # semicolon is optional in python prg. break keyword is used to break the line.
    print(student)

for student in students:
    if student == "Kishan":
        continue; # continue is used to skip.
    print(student)