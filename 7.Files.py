#Learning about files!

#Opening a File using open()
# handle = open(filename, mode)


#Searching through a file
ze_file = open('test.txt')
for line in ze_file:
    line = line.rstrip()
    if line.startswith('Most'):
        print(line)


#Prompt for file name & try to catch a bad file name
'''
fname = input("Please enter the file name: ")
try:
    fhand = open(fname)
except:
    print("This File cannot be opened:",fname)
    exit()
count = 0
for line in fhand:
    if not "you" in line:
        continue
    print(line.upper())
'''

# Use the file name mbox-short.txt as the file name
'''
fname = input("Enter file name: ")
total = 0
occurence = 0
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line_improved = line.find(" ")
    line_final = line[line_improved:].strip()
    line_final = line_final.strip()
    number = float(line_final)
    occurence += 1
    total = total + number
final_total = total / occurence
print("Average spam confidence:", final_total)
'''


