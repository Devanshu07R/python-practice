#Code implementation for the exception handling in python

a = int(input("Input the value of a:"))
b = int(input("Input the value of b:"))
try:
    c = a/b
    print("Result:", c)
except:
    print("OOps it's not divisible by b")
else:
    print("Successful, it's divisible by b")