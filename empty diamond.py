# row=0
# while row<5:
#     col=0
#     while col<5:
#         if row+col==2 or col-row==2 or row-col==2 or col+row==6:
#             print("*",end=" ")
#         else:
#             print(end=" ")    
#         col+=1
#     row+=1
#     print()        
            
            
#  OUTPUT 
#      *
#     *  *
#    *     *
#     *   *
#       *


            
# row=0
# while row<5:
#     col=0
#     while col<5:
#         if row+col==2 or col-row==2 :
#             print("*",end=" ")
#         else:
#             print(end=" ") 
#         col+=1
#     row+=1
#     print()                
    
    
    
# row=0
# while row<5:
#     col=0
#     while col<5:
#         if row-col==2 or col+row==6 :
#             print("*",end=" ")
#         else:
#             print(end=" ") 
#         col+=1
#     row+=1
#     print()         


# row=0
# while row<=5:
#     col=1
#     while col<=5:
#         if   col+row==5 or row-col==5 :
#             print("*",end="  ")
#         else:
#             print(end="  ") 
#         col+=1
#     row+=1
#     print()     


# row=3
# for i in range(row):
#     for j in range(row-i):
#         print(' ', end='') 
#     for j in range(2*i+1):
#         if j==0 or j==2*i or i==row-1:
#             print('*',end='')
#         else:
#             print(' ', end='')
#     print() 


# a=[1,2,3,4]
# b=a
# print(a is b,a==b)




# a="Generally jab hum koi bhi  website ke servers pe bahot load padta hai. Abhi toh aap sirf bahot thodi"
# i=0
# count=0
# while i<len(a[i]):
#     if count==15:
#         print()
#     else:  
#         count+=1
#     i+=1
# print(a)    

# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j+=1
#     print()
#     i+=1

# i=1
# while i<=6:
#     j=1
#     while j<=6:
#         if (i+j==3) or (j-i==3) or (i+j==9) or (i-j==3):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#         j+=1
#     i+=1
#     print()
    
# for i in range(7):
#     for j in range(7):
        
#         if (i+j==3) or (j-i==3) or (i+j==9) or (i-j==3):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
    
    
# for row in range(1,5):
#     for col in range(1,8):
#         if row==4 or row+col==5 or col-row==3:
#             print("*",end="") 
#         else:
#             print(end=" ") 
#     print()  
           
           
# i=1
# while i<5:
#     j=1
#     while j<8:
#         if i==4 or i+j==5 or j-i==3:
#             print("*",end="") 
#         else:
#             print(end=" ") 
#         j+=1
#     print()    
#     i+=1    

 
# i=0
# while i<5:
#     j=1
#     while j<5:
#         if j==4 or i==1:
#             print("*",end=" ")
#         else:
#             print(end=' ')
#         j+=1
#     print()    
#     i+=1           
        
      
# a = " Hello, World! "
# print(a.strip()) # returns "Hello, World!" 


# a = "Hello, World!"
# print(a.replace("H", "J"))


# a=" pinki mandal"
# # print(a)
# print(a.strip()) 


# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x) 

# PEP stands for Python Enhancement Proposal,
# it is a document that provides guidelines and best practices on how to write Python code. 





# x="ram"
# def fun():
#     global x
#     y="syam"
#     print(x)
#     print(y)
# fun()    

# a=("appel","banana","cherry")
# print(a[1])

# a={"apple","banana","cherry"}
# print(a[1])



    # ```List is a collection which is ordered and changeable. Allows duplicate members.
    # Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    # Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    # Dictionary is a collection which is ordered** and changeable. No duplicate members.

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])

# a=["pinki","mandal"]
# a[1]="neha"
# print(a)

# a=["pinkk","mandal","neha"]
# a.insert(1,"mon")
# print(a)

# a=["pinki","mandal"]
# a.append("mondadd")
# print(a)


# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# del thislist 


# a=["pinki","mandsal","neha"]
# a.append("xdfcgv")
# print(a)


# a={"a":{"b":5,"c":2}}
# for i in a:
#     for j in a[i]:
#         print(a[i][j])

# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.


# num=int(input("enter the number"))
# if num%2==0:
#     print("num")
# if num%3==0:
#     print("gurukul")  
# if num%5==0:
#     print("navgurukul")  
# else:
#     print("nothing") 
    
    
    
    
# num=int(input("enter the number"))
# if num%5==0:
#     print("navgurukul")
# if num%3==0:
#     print("gurukul")  
# if num%2==0:
#     print("num")  
# else:
#     print("nothing") 


# i=int(input("enter the number"))
# r=0
# x=i
# while i>0:
#     r=r*10+i%10
#     i=i/10
# if i%5==0:
#     print("not pallindrome")
# else:
#     print("pallindrome")        
    
    



# i=int(input("enter the number"))    
# fac=1
# while i>0:
#     fac=fac*i
#     i=i-1
# print(fac)  


# r=0
# while r<5:
#     c=0
#     while c<5:
#         if r+c==2 or c-r==2  or r==5:
#             print("*",end=" ") 
#         else:
#             print(" ",end=" ") 
#         c+=1
#     r+=1
#     print()            

# r=0
# while r<5:
#     c=0
#     while c<5:
#         if r+c==2 or c-r==2 or c+r==6 or r-c==2:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ") 
#         c+=1
#     r+=1
#     print()           





# i=int(input("enter the number"))
# fac=1
# while i>0:
#     fac=fac*i
#     i=i-1
# print(fac)    

# i=int(input("enter the numebr"))
# r=0
# x=i
# while i>0:
#     r=r*10+i%10
#     i=i//10
# if x==r:
#     print("pallindrome number") 
# else:
#     print("not pallindrome number")       
    
    
# num=int(input("enter the numbe")) 
# x=1
# y=0
# z=1
# while num>z:
#     print(z) 
#     x=y
#     y=z
#     z=x+y  

