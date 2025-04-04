x =int( input ("Inter your value") )
for i in range (1,x+1):
    for j in range (1 , x+1):
        if i == j:
            print (f"{i}*{j}={i*j}")
            break
        print (f"{i}*{j}={i*j}")