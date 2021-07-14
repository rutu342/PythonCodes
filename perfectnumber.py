n=int(input("enter any number"))
i=1
sum=0
while(i<n):
    if(n%i==0):
        sum=sum+i#1 3 6 10 15 21 28
    i=i+1#2 3 4 5 6 7
if(sum==n):
    print("perfect number")
else:
    print("not a perfect number")
