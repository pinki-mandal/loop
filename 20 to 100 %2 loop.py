# i=20
# while i<=100:
#     if i%2==0:
#         print(i)
#     i=i+1    
# else:
#     i=i+1    

# num=int(input("enter the number"))
# a=[7,2,1,4,5]
# i=0
# while i<len(a):
#     if num!=a[i]:
#         print(num+1)
#         break
#     else:
#         print("nothing")
#     i=i+1
# print(num+1)
    # num=num+1
# print(num)


# a=[2,3,8,7,2]
# num=int(input("enter the number"))
# i=0
# while i<len(a):
#     if num<a[i]:
#         num=a[i]
#         print(a[i+1])
#     i+=1


# a=[2,3,8,7]    
# num=int(input("enter the number"))
# i=0
# b=[]
# j=0
# while i<len(a):
#     if num<a[i]:
#         num!=a[i]
#         j=a[i+1]
#         b.append(j)
#         j+=1        
#     i+=1
# print(b)        
    
list1=[1,2,3,4,5,6] 
list2=[2,3,1,0,6,7]  
b=[] 
i=0
while i<len(list1):
    if list1 not in  list2:
        b.append(list1)
    i+=1
print(b)        
        