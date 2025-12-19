import sys

n = int(input())
if not (1<=n<=20):
    print("Invalid Input")
    sys.exit()

for i in range (0,n):
    print(i*i)