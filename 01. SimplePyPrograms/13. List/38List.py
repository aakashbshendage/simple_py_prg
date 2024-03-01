# Prg for List DataType. List is used to store collection of data. 

marks = [ 95, 98 , 97] # [] is used for list.
print(marks)

# Using for loop to print list.

for score in marks:
    print(score)

# Using operations.

marks.append(99) # append is used to add.
print(marks)

marks.insert(0, 96) # insert is used to add number in a particular index.
print(marks)

print(96 in marks) # in used to check the value is vailable in list. If yes then value output will be true.

print(len(marks)) # len is used to print length of the string.