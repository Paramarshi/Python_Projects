import sys
n= int(input())
if not (1<=n<=100):
    print("Invalid Input!")
    sys.exit()

if (n%2==0) and (n not in (6, 8, 10, 12, 14, 16, 18, 20)):
    print("Not Weird")
else:
    print("Weird")


