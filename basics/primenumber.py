a = int(input("Enter number "))

if(a<2):
     print("not prime")
for i in range(2,a):
    if a%2==0:
        print("not prime")
        break
else:
        print("prime")