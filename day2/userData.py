import re
def userData():
    while True:
        name=input("enter your name: ")
        if name.isalpha():
            break
        print("error, Please enter valid name.")
    email_pattern = r'^[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]{2,}$'
    while True:
        email = input("enter your email: ")
        if re.match(email_pattern, email):
            break
        print("Invalid email. Please enter a valid email address.")
    
    return name, email
name, email = userData()
print(name,email)