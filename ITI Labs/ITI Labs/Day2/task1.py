#Mario Prymid with lists

prymid = [" "," "," "]
for i in range (len(prymid)) :
    prymid.pop()
    prymid.insert(len(prymid)-i-1 , "#")
print (prymid)
