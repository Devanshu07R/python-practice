# to find the greatest number among trhe three...
a = int(input("Enter the 1st number:"))
b = int(input("Enter the 2nd number:"))
c = int(input("Enter the 3rd number:"))

if(a>b and a<c):
    print(a,'is the greatest number.')
elif(b>a and b>c):
    print(b,'ius the greatest number.')
else:
    print(c,'is the greatest number.')