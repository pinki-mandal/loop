n=int(input("enter the number"))
i=1
while i<=1:
    if n%4==0 or n%100==0 or n%400==0:
        print("leap year")
    else:
        print("not leap ")
    i=i+1     