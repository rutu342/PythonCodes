sum=0
#to check wether number is armstrong number or not
n=int(input("enter any number"))
p=n
i=0
while(n>0):
    x=n%10
    sum=sum+x*x*x
    n=int(n/10)
    i=i+1
if(sum==p):
     print("Armstrong number")
else:
     print("not an armstrong number")




