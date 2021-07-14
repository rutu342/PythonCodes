sum=0
n=int(input("enter number"))
i=0
p=n
while(n>0):
    x=n%10
    sum=sum*10+x
    n=int(n/10)
    i=i+1
if(p==sum):
    print("palindrome number")
else:
    print("Not a palindrome number")


