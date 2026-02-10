# nested if statements
# A nested if statement is an if statement that is combined within another if statement

age = 29
weight = 32

if age > 15:
    if weight > 50 :
        print("you can donate blood")
    else:
        print("you cannot donate blood because of your weight")    
else:
    print("you cannot donate blood because of your age")        