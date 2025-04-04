users = [{"name":"omar","password":"123"},{"name":"ahmed","password":"442"}]

def validation (name,password):
    for i in range (len(users) ):
        if users[i]["name"].lower() == name.lower() and users[i]["password"] == str(password) :
            return f"Weclome to the system,{name} "
        else :
            return "Incorrect name or password"
        
username = input ("Please enter your name :")
password = input ("Please enter your password:")

print (validation(username , password))