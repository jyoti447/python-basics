a =int(input("enter number 1 : "))
b =int(input("enter number 2 : "))
c =int(input("enter number 3 : "))
if (a>b) & (a>c):
    print(" a is greatest")
elif (b>c) & (b>a):
    print("b is greatest")

else:
    print("c is greatest")