#checking if its number and dont get out untill it gives me a number

num = input ("enter number:")

while not num.isdigit():
    num = input ("please enter a valid num:")
    
num = int (num)