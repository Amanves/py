a = int(input("Enter any number "))
for i in range(1,a+1):
    for j in range(1,a-i+1):
        print(" ",end="")
    for j in range(i,0,-1):
        print("#",end="")
    for j in range(2,i+1,1):
        print("#",end="")
    print()