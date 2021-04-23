#to find greater number using three variables
a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
if(a>b):
    if(a>c):
        print(a,"is greater than",b,"and",c)
elif(b>a):
    if(b>c):
        print(b,"is greater than",a,"and",c)
    else:
       print(c,"is greater than",a,"and",b)

