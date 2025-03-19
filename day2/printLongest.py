def printLongest():
    text=input("enter a text")
    longest = current = text[0]
    for i in range(1, len(text)):
        if text[i] >= text[i-1]:
            current += text[i]
        else:
            current = text[i]
        if len(current) > len(longest):
            longest = current
    return longest
print(printLongest())