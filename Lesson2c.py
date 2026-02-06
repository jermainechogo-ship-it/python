# A dictionary is a data tyoe that stores data in  terms of key - value pair
# It is introducedby the use of the curly braces {}
# The values stored inside of a dictionaary can be of any data type .
# to access the values in adictionarybwe use the keys


phonebook = {
    "Benson" : "0734564326",
    "Mary" : "075675456",
    "Joseph" : "074567890"
}

print(phonebook)
print(type(phonebook))

# print out persons number
print(phonebook["Benson"])


print("==========================")

player = {
    "name" : "messi",
    "age" : 40,
    "teams" : ["PSG","BARCELONA","ARGENTINS"]
}
# print bellow - the second team he played

print(player["teams"][1])

print("==========================")
planets = ("mercury","venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune")
print(type(planets))
print(planets)
print(planets[2:6])