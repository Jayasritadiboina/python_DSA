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
    print("done")'''''

#to throw error
a =int(input("enter a number:"))
if a<0:
    raise ValueError("number i negative")
else:
    print(a)