n1 = int(input("Enter the number of rows:"))

for i in range(n1, 0,-1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()

n2 = int(input("Enter the number of rows:"))
for i in range(1, n2+1):
    for j in range(1, i+1):
        print("$", end = " ")
    print()