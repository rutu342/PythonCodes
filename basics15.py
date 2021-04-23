act=30
spo=20
ex=50
totalact=60
totalspo=50
totalex=200
e1=int(input("enter score of 1st examination out of 100:"))
e2=int(input("enter score of 2nd examination out of 100:"))
sp1=int(input("enter score obtained in sports activities out of 50:"))
ac1=int(input("enter score obtained in activity 1 out of 20:"))
ac2=int(input("enter score obtained in activity 2 out of 20:"))
ac3=int(input("enter score obtained in activity 3 out of 20:"))
examtotal=e1+e2
acttotal=ac1+ac2+ac3
examper=float(examtotal*ex/totalex)
spoper=float(sp1*spo/totalspo)
actper=float(acttotal*act/totalact)
totalpercent=float(examper+spoper+actper)
print("\n\n*********************RESULT**************************")
print("\npercentage in examination",examper)
print("\npercentage in sports",spoper)
print("\npercentage in activities",actper)
print("\n---------------------------------------------------------")
print("\nTotal percentage",totalpercent)
