# python lists
# List in python is a collection of items that ordered in a certain way
# A list is introduced by the use of the square brackets{}
# the  items of a list are stored inside of indexes. Note: in programing we start counting from index zero(0) . 
# A list is mutable ie the contents can be changed

cars = ["BMD","BENZE","TOYOTASUPRA","NISSAN GTR","ROLS ROYS",]

print(cars)
print(type(cars))


# accessiing items of a list
print(cars[2])
print("The car on index four is:", cars[4])

# Lisy slicing - this is creating a list from a given bigger list
print(cars[4:])

# printing from index zero to three
print(cars[:4])

print(cars[2:])

# List - mutabilty
# we use the function append to add an item at the ens  of the list
cars.append("lambogini")
print(cars)

cars.append("subaru")
print(cars)

# We use the  pop function to remobe an item from the enene of the  list
cars.pop()
print(cars)

# Wecan use an index to add items on our list
cars[5] = "porsh"
print(cars)

# We can use the sort fuction to sort ower items in alphabetical order
cars.sort()
print(cars)