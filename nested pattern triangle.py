# i=1
# while i<=6:
#     j=1
#     while j<=i:
#         print("*",end="")
#         j=j+1
#     print() 
#     i=i+1   


# output#
# *
# **
# ***
# ****
# *****

i=1
while i<=6:
    j=1
    while j<=i:
        print(j%2,end=" ")
        j=j+1
    print()
i=i+1       