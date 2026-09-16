n1=int(input("Enter the number 1: "))
n2=int(input("Enter the number 2: "))
n3=int(input("Enter the number 3: "))
if(n1>n2):
    if(n1>n3):
        print("Greatest number is n1: ",n1)
    else:
        print("Greatest number is n3: ",n3)
else:
    print("Greatest number is n2: ",n2)