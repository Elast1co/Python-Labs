#List in a List problem
big_list =[]

x = input ("Inter your value")
x = int(x)
for i in range (1,x+1):
    s_list =[]
    for j in range (1 , i+1):
        s_list.append(j*i)
    big_list.append(s_list)

print (big_list)

