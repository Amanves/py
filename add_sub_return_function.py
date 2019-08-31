def add_sub(x,y):
    c = x+y
    if x>y:
        d = x-y
    else:
        d = y-x
    return c,d
result1,result2 = add_sub(4,5)
print(result1,result2)
