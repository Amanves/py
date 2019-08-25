for row in range(7):
    for col in range(5):
        if (col==0 or col==4) or ((row==1 and ((col==1) or (col==3)) or ((row==2) and (col==2))) and (col>0 and col<4)) :
            print("*",end="")
        else:
            print(end=" ")
    print()