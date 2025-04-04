users = [{"name":"omar","password":"123"},{"name":"ahmed","password":"442"}]
        
user = input ("Please enter your name :")
password = input ("Please enter your password:")

for i in range(len(users) ):
    if users[i]["name"].lower() == user.lower() and users[i]["password"] == str(password) :
        print( f"Weclome to the system,{user} ")
        break
    else :
        continue
else:
    print("un auth")
        


