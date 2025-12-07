a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
c=int(input("enter 3rd number"))
if (a>=b) and (a>=c):
    print("Maximum number is:", a)
elif (b >= a) and (b >= c):
    print("Maximum number is:", b)
else:
    print("Maximum number is:", c)
