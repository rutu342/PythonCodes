n=int(input("enter limit"))
n1=1
for i in range(n1,n):
    count=0
    p=2
    n1=n1+1
    while(p<=n1/2):
        if(n1%p==0):
            count=count+1
            break
        p=p+1
    if(count==0 and n1!=1):
        print(n1)

