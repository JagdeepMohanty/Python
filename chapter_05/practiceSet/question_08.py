# If languages of two friends are same; what will happen to the program in problem 6?
s={}
keys=["jadeep","jagu","jaggi","jam"]
value=["english","odia","odia","gujrati"]

s=dict(zip(keys,value))
 

print(s)   #{'jadeep': 'english', 'jagu': 'odia', 'jaggi': 'odia', 'jam': 'gujrati'}

#as keys are unique it is printing all the values even it is same 
# In this case, since the languages "odia" is repeated, the dictionary will still keep all entries because the keys (names) are unique.