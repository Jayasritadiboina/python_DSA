n=5
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()
#right angled triangle
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
#inverted right angled triangle
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()
#diamond pattern 
n = 5
# Upper part
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
# Lower part
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

#AMSTRONG NUMBER
#153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153
n=int(input("enter a number: "))
temp = n                             #temp=temparary variable
sum = 0
while temp>0:
    digit =temp%100
    sum +=digit**3
    temp//=10
if sum==n:
    print(n,"is an Armstrong number")
else:
    print(n,"is not an Armstrong number")

#hollow  Square pattern
n=10
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or j==n-1 or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#pascal patterns
num = 1
for i in range(0,5):
    for j in range(0,i+1):
        print(num, end=" ")
        num += 1
    print()










