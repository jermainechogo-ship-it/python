# Nhif Assignment
grosssalary = int(input("enter gross income"))
# Print monthly contributions
if grosssalary < 5999 :
    print(150.00)
elif grosssalary >= 6000 and grosssalary < 7999 :
    print(300.00)
elif grosssalary >= 8000 and grosssalary < 11999 :
    print(400.00)    
elif grosssalary >= 12000 and grosssalary < 14999 :
    print(500.00)    
elif grosssalary >= 15000  and grosssalary < 19999 :
    print(600.00)   
elif grosssalary >= 20000  and grosssalary < 24999 :
    print(750.00)    
elif grosssalary >= 25000 and grosssalary < 29999 :
    print(850.00)    
elif grosssalary >= 30000 and grosssalary < 49999 :
    print(10000.00)    
elif  grosssalary >= 50000 and grosssalary  < 99999 :
    print(15000.00)    
else :
    print(2000.00)    