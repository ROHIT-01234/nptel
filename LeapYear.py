y=int(input("Enter a Year : "))

""" if (y%400==0):
    print(y,"is a Leap Year.")
elif (y%100==0):
    print(y,"is a not Leap Year.")
elif (y%4==0):
    print(y,"is a Leap Year.")
else:
    print(y,"is a not Leap Year.") """

if(y%4==0 and y%100!=0 or y%400==0):
    print(y,"is a Leap Year.")
else:
    print(y,"is not a Leap Year.")