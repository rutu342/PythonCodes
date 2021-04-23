#write a program to calculate average of two numbers and print their deviation
num1=int(input("enter first number"))
num2=int(input("enter second number"))
avg=(num1+num2)/2
dev1=num1-avg
dev2=num2-avg
print("average",avg)
print("deviation",dev1,dev2)
