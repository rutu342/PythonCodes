#to find total salary of employee where acc=7% pf=9% transport=7% hra=5%
salary=float(input("enter salary"))
hra=0.05*salary
ta=0.07*salary
acc=0.07*salary
pf=0.09*salary
total=salary+hra+ta+acc-pf
print("Total salary of employee is",total)
