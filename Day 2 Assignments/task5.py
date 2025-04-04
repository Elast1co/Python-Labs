n = 5
pyramid = []

for i in range(1, n + 1):
    spaces = [" "] * (n - i)  
    hashes = ["#"] * i  
    row = spaces + hashes 
    pyramid.append(row)  


for row in pyramid:
    print(row)  
