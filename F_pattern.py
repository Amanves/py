for row in range(1,8):
    for col in range(1,5):
        if (col==1) or (((row==1) or (row==3)) and (col>1)):
            print("*",end="")
        else:
            print(end=" ")
    print()