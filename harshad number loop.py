# n=int(input("enter the number"))
# i=n
# s=0
# while i>0:
#     s=s+(i%10)
#     i=i//10
# if n%s==0:
#     print("harshad number")
# else:
#     print("not harshad number")    
    
    
n=int(input("enter the number"))
r=0
i=n
while i>0:
    r=r*10+i%10
    i=i/10
if n%r==0:
    print("harsed number")
else:
    print("not harsed number")        
    
    
        