
#Definite Looping Through Strings
    # 1)Definite loop using for..in is much more elegant.
fruit = "banana"
index = 0
for letter in fruit:
    print(letter)

#Slicing strings
s = "Hello World"
print(s[0:4])
print(s[:2])

#String Concatenation
a = 'Hello'
b = a + ' There'
print(b)

#String Comparison
word = "banana"
if word == "banana":
    print("Alright, banana")

#Stripping Whitespace
    # 1) using lstrip or rstrip or strip

#Prefixes
    # 1) x.startwith, check if it starts with a specific word
x = 'From marquard@uct.ac.za'
print(x[14:17])

text = "X-DSPAM-Confidence:    0.8475";
text_improved = text.find(" ")
text_final = text[text_improved:].strip()
text_final = text_final.strip()
print(text_final)
