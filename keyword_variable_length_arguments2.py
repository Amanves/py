def person(name,**data):
    print(name)
    for i,j in data.items():  #item() is a pre-defined function.
        print(i, "=" ,j)      #i and j are key and value pair.
                              #i represents key like add, age and mob.
                              #j represents its value.
person("Aman",add="Kolkata",age=21,mob=987654321)