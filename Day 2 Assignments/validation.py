while True:
    email = input ("Enter your email:")
    if '@' in email and '.' in email:
        username , domain = email.split ('@')
        if username and domain:
            x,y = domain.split ('.')
            if x and y :
              break
    else :
        print ("Please enter a valid email adress")

print ("Email", email)