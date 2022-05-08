row=0
while row<6:
    coloum=0
    while coloum<7:
        if (row==0 and coloum%3!=0) or (row==1 and coloum%3==0) or (row-coloum==2) or (row+coloum==8):
            print("*",end="  ")
        else:
            print(end="  ") 
        coloum=coloum+1
    print() 
    row=row+1    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # output #
    #  *  *     *  *
    # *      *       *
    # *             *
    #   *          *
    #      *     *
    #          *