a=int(input("ENTER A FIRST SIDE OF A TRIANGLE:"))
b=int(input("ENTER A SECOND SIDE OF A TRIANGLE:"))
c=int(input("ENTER A THIRD SIDE OF A TRIANGLE:"))
if((a+b)<=c):
    print("!!!INVALID!!!")
elif(a==b or b==c or a==c):
    print("ISCOSCELES TRIANGLE")
elif(a!=b or b!=c or a!=c):
    print("SCALENE TRIANGLE ")
else:
    print ("RIGHT ANGLE TRIANGLE")
