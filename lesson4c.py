# a for loop can also be used to iterate through a list, tuple, strings or even adictionary...

name = "jermaine"

for letter in name:
    print(letter)
    if letter == "n":
        print("this letter is n")
    else:
        print(letter) 

print("==========================")           
# below is a list of counties
counties = ["nairobi","kagiado","mombasa","nakuru","meru","embu"]

print(counties)

for county in counties:
    print(county)

print("========================") 
for county in counties:
    if county == "nairobi":
        print("the county is part of list")  
        break
    else:
        print("the county is not part of the list")     



print("========================") 
# the for loop can also be used to italate through a dictionary


player ={
    "name" : "mbape",
    "age" : 25,
    "teams" : ["pdg","monaca","france"],
    "nationalty" : "french"
}
for key in player:
    print(key)

    print("========================") 
    for values in player:
        print(player[values])

print("========================") 
 # loop through the teams the player has played for
for team in player["teams"]:
    print(team) 