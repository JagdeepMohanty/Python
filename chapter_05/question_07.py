# If the names of 2 friends are same; what will happen to the program in problem 6?

s={}
keys=["jadeep","jaggi","jaggi","jam"]
value=["english","marathi","odia","gujrati"]

s=dict(zip(keys,value))
 

print(s)


# In this case, since the name "jaggi" is repeated, the dictionary will only keep the last entry for that key.