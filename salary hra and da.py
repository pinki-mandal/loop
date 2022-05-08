basic_salary=int(input("enter the number"))
if basic_salary<=10000:
    hra=basic_salary*0.8
    print(hra)
    da=basic_salary*0.2
    print(da)
elif basic_salary<=20000:
    hra=basic_salary*0.25
    print(hra)
    da=basic_salary*0.9
    print(da)
elif basic_salary>=20000:
    hra=basic_salary*0.3
    print(hra)
    da=basic_salary*0.95 
    print(da)   
    gross_salary=basic_salary+da+hra    
else:
    print("nothing")
    
