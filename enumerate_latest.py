# Python program to illustrate enumerate function
# enumerate function adds a counter to an iterable and returns it (the enumerate object is returned)
# Syntax -> enumerate(iterable, start=0)

l1 = ["eat", "sleep", "repeat"]
s1 = "aks"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

print ("Return type:", type(obj1))
print (list(enumerate(l1)))

# changing start index to 2 from 0
print (list(enumerate(s1, 2)))

# Python program to illustrate
# enumerate function in loops
l2 = ["eat", "sleep", "repeat"]

# printing the tuples in object directly
for ele in enumerate(l2):
	print (ele)

# changing index and printing separately
for count, ele in enumerate(l2, 100):
	print (count, ele)

# getting desired output from tuple
for count, ele in enumerate(l2):
	print(count)
	print(ele)

