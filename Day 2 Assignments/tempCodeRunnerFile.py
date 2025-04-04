
number_list =[]
for i in range (5):
    numb = input (f"enter your numb {i+1} :")
    numb = int (numb)
    number_list.append (numb)

    asc = sorted(number_list)
    dsc = sorted(number_list, reverse=True)
    

print (number_list)
print (dsc)
print (asc)
