n=int(input("enter number"))
i=2
while(i<n):
    if(n%i==0):
        print("number is not prime")
        break
    i=i+1
    if(n==i):
        print("number is prime")
