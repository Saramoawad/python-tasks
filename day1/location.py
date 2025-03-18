string = input("enter string : ")
locations=[]
for index in range(len(string)):
    if string[index]=='i':
        locations.append(index)
print(locations)