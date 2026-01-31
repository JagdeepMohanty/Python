# Can you change the values inside a list which is contained in set S?
s = {8, 7, 12, "Harry", [1,2]}

s.add[1,2,3]
print(s)   #TypeError: cannot use 'list' as a set element (unhashable type: 'list')


#no, it is showing error and type error of unhasable