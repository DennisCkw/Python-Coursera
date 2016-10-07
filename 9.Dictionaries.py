#Dictionaries

#Dictionaries are just like List but they have a label. They also don't have any order, they use a method called Hash which is also much faster.
#Dictionaries are like histogram, really good at counting/keeping track of stuff.

phoneBook = {'jack':1111, 'bob':2222, 'jane':3333}
print(phoneBook)
print(phoneBook['jack'])

if 'jack' in phoneBook:
    print("Yes it is!")

#This is easier to define a dictionary
phoneBook2 = dict(bob=1111, lel=2222, kiddo=3333)
print(phoneBook2)

phoneBook2['bob'] += 100
print(phoneBook2)

#get method
#print count.get(name, 0)
# - prints the number of the key. If doesn't exist, then print 0.

#To get the key
#print jjj.key()
#print jjj.items() - get both key & value

#Looping Techniques in Dict
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

#Assignment 1
fh = open("test.txt")
zeDict = dict()
for line in fh:
    line = line.rstrip()
    word = line.split()
    if not word or word[0] != "From": #"if not word" --> checks if empty list
        continue
    zeDict[word[1]] = zeDict.get(word[1],0) + 1
print(zeDict)

bigWord = 0
bigCount = 0

for word, count in zeDict.items():
    if count > bigCount:
        bigCount = count
        bigWord = word
print(bigWord, bigCount)
