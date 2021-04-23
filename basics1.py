#program to reverse a 3 digit number
a=123
b=a%10#3
c=int(a/10)#12
d=c%10#2
e=int(c/10)#1
total=b*100+d*10+e
print(total)
