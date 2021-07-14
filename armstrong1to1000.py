n2=int(input("enter limit"))
#to print armstrong number till 1 to 1000
n1=1
while(n1<n2):
    p=n1
    sum=0
    while(p>0):
        x=p%10
        sum=sum+x*x*x
        p=int(p/10)
    if(n1==sum):
        print(n1)
    n1=n1+1
