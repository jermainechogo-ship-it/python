# loops --> sometimes we may need  it to a piece of work a number of repeated times in such caeses we may use loops
# A loop is a controle structure that allows us to repeat a block of code as long as  a specified condition is true
# There are two types of loops in python i.e the for loop and the while loop



# below is the syntrax of a loop in python
"""""
for variable in range(n):
    # block of code to be executed
"""""


for greeting in range(5):
    print("hello there moses",greeting)


    print("====================================")

    for number in range(10,20):
        print(number)
print("==========================")
# find the even number in the range of 50 to 71
for number in range(50,71,2):
    print(number) 
    

    print("====================")
    
# create a python program that prints the oddd numbers from 100to 150
for number in range(101,150,2):
    print(number)

    print("==========================")

    
for number in range(201,150,3):
        print(number)

print("=========================")        
# create a python program that prints the leap years in between 2000 and 2024
for years in range(2000,2024,4):
     print(years)
