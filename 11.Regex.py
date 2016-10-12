#RegEx
#It iself is a tiny programming language that can be used in other languages.
#Used when solving/parsing/matching complex strings

# ^ --> starts with
# . --> matches character
# * --> any number of times (everything)
# \S --> any non-whitespace character
# .+ --> greedy matching
# .+? --> non-greedy matching
import re
'''
#re.search() returns T/F
file = open('test.txt')
for line in file:
    line.rstrip()
    if re.search('^From:', line):
        print(line)

#re.findall() --> puts into a list
x = "2 + 1 = 3...lalalalal"
y = re.findall('[0-9]+', x) #find 0-9 number or more
print(y)
'''
#greedy matching
#If you have a longer string, take the longer.
with open('test.txt', 'r') as myFile:
    data = myFile.read()
y = re.findall('^From (\S+@\S+)', data, re.MULTILINE)
#print(y)

x = re.findall('^From .*@([^ ]*)', data, re.MULTILINE)
print(x)


