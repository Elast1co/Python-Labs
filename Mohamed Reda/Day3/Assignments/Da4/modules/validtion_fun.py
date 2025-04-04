def get_valid_name():
    while True:
        try:
            name = input("Enter your name: ")
            if name.replace(" ", "").isalpha():  # Allow spaces in names but only letters
                return name
            else:
                raise ValueError("Invalid name! Please enter only letters.")
        except ValueError as e:
            print(e)

def get_valid_email():
    while True:
        try:
            email = input("Enter your email: ")
            if "@" in email and "." in email:  
                at_index = email.index("@")
                dot_index = email.rindex(".")  # Use rindex to find last occurrence of '.'
                if at_index < dot_index:  # '@' must come before '.'
                    return email
            raise ValueError("Wrong email format! Please write the email correctly.")
        except ValueError as e:
            print(e)


