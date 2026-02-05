# Tuple
# A tuple is an immmutable type of list (it cannoyt change)
# To introduce a tuple , we use the parenthesis()

counties = ("Nairobie", "Kisumu","Eldoret","Mombasa")
print(type(counties))
print(counties)

# slicing in tuples
print(counties[3:1])

# accessing items of a  tuple by useof index
print(counties[5])

# note: bellow will generate an error
# atribute error
counties.append("Kajiado")
print(counties)