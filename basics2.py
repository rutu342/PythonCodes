#reverse a 4 digit number
a=int(input("enter a 4 digit number"))#1234
b=a%10#4
c=int(a/10)#123
d=c%10#3
e=int(c/10)#12
f=e%10#2
g=int(e/10)#1
total=b*1000+d*100+f*10+g
print(total)
