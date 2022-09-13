#program to check the given number is positive or negative or zero
x=int(input("Enter a number: "))
if x>0:
    print("%d is positive number"%x)
elif x<0:
    print("%d is negative"%x)
else:
    print("%d is zero"%x)