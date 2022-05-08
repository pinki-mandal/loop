# num=int(input("enter the number:"))
# i=1
# count=0
# while i <=(num):
#     if num%i==0:
#         count+=1
#     i+=1
# if count==2:
#     print("prime number")
# else:
#     print("not prime number") 

num=int(input("enter"))
i=1
count=0
while i<=num:
    if num%i==0:
        count+=1
    i+=1
if count==2:
    print("prime nuber")    
        
        
    
 
# num=int(input("enter the number:"))
# b=[] 
# i=1
# count=0
# while i<=10:
#     if num%i==0:
#         count+=1
#     i+=1
#     b.append(num)
# if count==2:
#     print("prime number")
# else:
#     print("not prime number") 
 
# num=int(input("enter the number:"))
# i=1
# count=0
# while i <=(num):
#     size=int(input("enter the size"))
#     if num%i==0:
#         count+=1
#     i+=1
# if count==2:
#     print("prime number")
# else:
#     print("not prime number") 
    
 
 
    
# 25801
# 963258


# your request not rececived from python_branch()

 
lower=int(input("enter the number"))
upper=int(input("enter the number"))
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
               break
        else:
           print(num)