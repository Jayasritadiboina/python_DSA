''''x=int(input("enter a number:"))
y=int(input("enter a number:"))
try:
    print(x/y)
except ZeroDivisionError as e:   #zerodiisionerror
    print(e)
except valueError as e:            #valueError
    print(e)
finally:                           #finally
    print("done")

#
for i in range(5):
    if i==4:
        break
    print(i)
else:
    print("done") 


#
try :
    a= int(input("enter a number:"))
    print(a)
except valueError as  e :
    print(e)
else:
    print("done")

#to throw error
a =int(input("enter a number:"))
if a<0:
    raise ValueError("number i negative")
else:
    print(a)'''''
#TASK1:##keep asking valid integer number
##if not valid integer number ,print error
while True:
    try:
        a=int(input("enter a number:"))
        print(a)
    except ValueError as e:
        print(e)
    else:
        print("done")
        break

#task2
#handle index error while accessing list,elements if it is out of range module it
L=[0,1,2,3,4,5,6,7,8,9,10]
try:
    print(L[10])
except IndexError as e:
    print(e)