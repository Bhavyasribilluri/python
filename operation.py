#to find the largest number
a=int(input("enter"))
b=int(input("enter"))
c=int(input("enter"))
d=int(input("enter"))
e=int(input("enter"))
if (a>=b) and (a>=c) and (a>=d) and (a>=e):
 print (a)
elif(b>=c) and (b>=d) and (b>=e):
 print(b)
elif(c>=d) and (c>=e):
 print (c)
elif(d>=e):
 print (d)
else:
    print(e)
