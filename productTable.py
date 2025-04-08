# Write a program to print 7 multiplication table..

#for number in range(1,11):
    #print(f"7 x {number} = {7 * number}")

#for number in range(1,11):
   #print(f"15 x {number} = {15 * number}")

for base in range(1,11):
    print(f"\nMultiplication Table of {base}:")

    for multiplication in range(1,11):
        print(f"{base} x {multiplication} = {base * multiplication}")