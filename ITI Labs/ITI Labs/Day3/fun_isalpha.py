def check_name(x):
  if x.isalpha():
    return print (f"Welcome:{x}")
  else :
    return "Wrong data , please enter your name"

name = input ("Pleaser Enter your name : ")
check_name(name)