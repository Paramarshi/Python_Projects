import sys

a= int(input())
b= int(input())
if not (1<=a<=10**10) or not (1<=b<=10**10):
    print("Invalid Input!")
    sys.exit()

print(a+b)
print(a-b)
print(a*b)