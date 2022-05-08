i=0
while i<7:
    j=0
    while j<5:
        if (j==0 or j==4)and(i!=0) or ((i==0 or i==3) and (j>0 and j<4)):
            print("*",end=" ")
        else:
            print(end="  ")
        j+=1
    print()    
    i+=1           
                