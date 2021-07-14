n2=int(input("enter limit"))
n1=10
while(n1<n2):
    sum=0
    p=n1
    while(p>0):
        x=p%10
        sum=sum*10+x
        p=int(p/10)
    if(n1==sum):
        print(n1)
    n1=n1+1
