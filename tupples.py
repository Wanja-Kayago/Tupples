Cars = ('Ford','Ferrari','BMW','Audi','Bentley','Chevrolet','Porche','Cadillac','Porche')
# finding a specific element in a tuple
print(Cars.index('BMW'))
print(Cars[1:3])
print(Cars[-8:-6])
print(Cars[1:])
#number of time a certain element has appeared in a list
print(Cars.count('Porche'))
#the length of a tuple
print(len(Cars))
#tuple sorted in ascending manner
print(sorted(Cars))
#the minimum element in the tuple
print(min(Cars))
#the maximum element in the tuple
print(max(Cars))
#converts an iterable object into a tuple
Brands = list(Cars)
print(Brands)
Cars = tuple(Brands)
print(Cars)
#Joining Tuples
Brands = ('Toyota','Honda','Nissan')
Cars += Brands
print(Cars)
#Comparing tuples
print(Brands<Cars)
#Add and delete an item in a tuple
print(Cars)
tupletolist = list (Cars)
print(tupletolist)
print(tupletolist.pop())
tupletolist.append('Prado')
print(tupletolist)
tupletolist.remove('Honda')
print(tupletolist)