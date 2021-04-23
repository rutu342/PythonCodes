#to check weather an alphabet is capital or small
alpha=input("enter any alphabet")
if(alpha>='a' and alpha<='z'):
    print(alpha,"is small")
elif(alpha>='A' and alpha<='Z'):
    print(alpha,"is capital")
else:
    print("Unknown value")
