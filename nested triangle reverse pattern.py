n=6
i=1
while i<=6:
    j=1
    while j<=n-i:
        print(i,end="") 
        j=j+1
    j=1
    while j<=6-i:
        print(" ",end="")
        j=j+1   
    print()
    i=i+1  
n=n-1 
     
#output  #  
# *****
# ****
# ***
# **
# *