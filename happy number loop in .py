num=int(input("enter the number"))
temp=num
rem=0
while sum!=1 and sum!=4:
    sum=0
    while temp!=0:
        rem=int(temp%10)
        sum=sum+rem*rem
        temp=temp//10
    temp=sum
if sum==1:
    print(num,"it is a happy number") 
    temp=temp+1
else:
    print(num,"is a sad number")        