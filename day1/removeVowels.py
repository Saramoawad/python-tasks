string=input("enter string : ")
vowels="aeiou"
newString=""
for char in string:
    if char not in vowels:
        newString+=char
print(newString)