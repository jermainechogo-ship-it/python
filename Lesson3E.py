# BELOEWW IS A GRADING SYSTEM BASEDON WHAT THE STUDENT MAY HAVE GOTTEN
marks = int(input("enter stucent marks: "))
# print("the entered Marksis",marks)
if marks > 0  and marks < 30 :
    print("below average")
elif marks >= 30 and  marks < 40 :
    print("average")    
elif marks >= 40 and marks < 70 :
    print("above average")    
elif marks >= 70 and marks < 100 :
    print("excelent")
elif marks < 0 :
    print("invalid input")    
else:
    print("invsalid input")   

     