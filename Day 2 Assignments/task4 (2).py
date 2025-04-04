while True:
    name = input("Enter your name: ")
    if name.replace(" ", "").isalpha(): 
        break
    print("Invalid name! Please enter only letters.")

while True:
    email = input("Enter your email: ")
    if "@" in email and "." in email:  
        at_index = email.index("@")
        dot_index = email.index(".")
        if at_index < dot_index:  # '@' must come before '.'
            break
    print("wromg email,Please write the email correctly.")

print("===== User Information =====")
print("Name:", name)
print("Email:", email)
print("Email is correct!")
