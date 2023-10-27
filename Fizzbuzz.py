a=int(input("Enter a Number:"))
for a in range(51):
    if (a%3==0 and a%5==0):
        print(a,"FizzBuzz")
    elif (a%5==0):
        print(a,"Buzz")
    elif (a%3==0):
        print(a,"Fizz")
    else:
        print(a,"Nor a FizzBuzz")
