n=int(input("enter any number"))
i=0
sum=0
while(i<n):
    if(i*i==n):
        print("perfect square")
        sum=sum+i
    i=i+1
if(sum==0):
    print("not a perfect square")
