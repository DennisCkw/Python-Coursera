#Tuples are like list but are immutable(cannot be changed).
# - cannot sort, append, add in tuples.
# - tuple is a reduction of list.

# But they are more  efficient, less processing time and less memory.
# Tuples are preferred when making 'temporary variables' over lists.

#Multi assign
x, y = (3, 4)
print(x, y)

#Tuples are comparable
z = (1, 2 ,3) < (2, 0 , 4)
print(z)

#Sorting Lists of Tuples
# - Use list to sort tuples
d = {'a':10, 'b':1, 'c':22}
l = d.items()
print(sorted(l))

