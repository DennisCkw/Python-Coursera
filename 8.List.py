#A list is a kind of collection
#- A collection is nice because we can have 1 variable carry many values
#- Strings are "immutable" - cannot change the contents of a string, must make a new string to make any change
#- Lists are "mutable" - can change an element of a list using the index operator

'''
x = [1,2,3]
print(x[0])
x[1] = 5
print(x[1])

# The range function returns a list of numbers that range from zero to one less than the parameter
x = range(4)
print(x)

for number in x:
    print("This many times")

x = list()
#print(dir(x))

#Strings and List
abc = "with three words"
stuff = abc.split()
print(stuff)
'''
#Assignment1
'''
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    words = line.split()
    print(words[0])
    for word in words:
        if word not in lst:
            lst.append(word)
print(lst)
'''
#Asssignment2
#fname = input("Enter file name: ")
fh = open("test.txt")
lst = list()
for line in fh:
    line = line.rstrip()
    word = line.split()
    if not word or word[0] != "From": #"if not word" --> checks if empty list
        continue
    lst.append(word[1])
print(lst)
count = len(lst)
print(count)