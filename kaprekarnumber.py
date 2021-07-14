#A kaprekar number 9 is a kaprekar number 9*9=81 8+1=9,45 is a kaprekar number
#its square is 2025 and addition of 2 digits is 20+25=45
#program to check wether the number is kaprekar or not
import math
n=int(input("enter number"))
N=n*n
k=n
c=0
while(k!=0):
    k=k/10
    c=c+1
p=int(N/math.pow(10,c))
q=(N%math.pow(10,c))
if(p+q==N):
    print("kaprekar number")
else:
    print("not kaprekar number")

